import os
import pathlib
import subprocess
import config
import driver
import time
from typing import List

__all__ = [
    "DriverLaGraph"
]


class DriverLaGraph(driver.Driver):
    """
    LaGraph library driver
    Use `BENCH_DRIVER_LAGRAPH` env variable to specify custom path to lagraph driver
    """

    def __init__(self, lagraph_build_root: pathlib.Path):
        self.exec_dir = lagraph_build_root / "src" / "benchmark"
        if not os.path.exists(self.exec_dir):
            raise Exception(f'LaGraph exec dir does not exist, where it should be: {self.exec_dir}')

        self.lagraph_bfs = "bfs_demo" + config.EXECUTABLE_EXT
        self.lagraph_sssp = "sssp_demo" + config.EXECUTABLE_EXT
        self.lagraph_tc = "tc_demo" + config.EXECUTABLE_EXT

        try:
            self.exec_dir = pathlib.Path(os.environ["BENCH_DRIVER_LAGRAPH"])
            print("Set lagraph exec dir to:", self.exec_dir)
        except KeyError:
            pass

    def name(self) -> str:
        return "lagraph"

    def run_bfs(self, graph: config.Graph, source_vertex, num_iterations) -> driver.ExecutionResult:
        with TemporarySourcesFile([source_vertex + 1] * num_iterations) as sources_file:
            output = subprocess.check_output(
                [str(self.exec_dir / self.lagraph_bfs), graph.path(), sources_file.name])
            return DriverLaGraph._parse_output(output, "parent only", 9, "warmup", 4)

    def run_sssp(self, graph: config.Graph, source_vertex, num_iterations) -> driver.ExecutionResult:
        with TemporarySourcesFile([source_vertex + 1] * num_iterations) as sources_file:
            output = subprocess.check_output(
                [str(self.exec_dir / self.lagraph_sssp), graph.path(), sources_file.name])
            return DriverLaGraph._parse_output(output, "sssp", 8)

    def run_tc(self, graph: config.Graph, num_iterations) -> driver.ExecutionResult:
        output = subprocess.check_output(
            [str(self.exec_dir / self.lagraph_tc), graph.path()])
        return DriverLaGraph._parse_output(output, "trial ", 2, "nthreads: ", 3)

    @staticmethod
    def _parse_output(output: bytes,
                      trial_line_start: str,
                      trial_line_token: int,
                      warmup_line_start: str = None,
                      warmup_line_token: int = None):
        time_factor = 1000
        lines = output.decode("ASCII").split("\n")
        trials = []
        for trial_line in lines_startswith(lines, trial_line_start):
            trials.append(float(tokenize(trial_line)[
                                    trial_line_token]) * time_factor)
        warmup = 0
        if warmup_line_start is not None:
            warmup = float(tokenize(lines_startswith(lines, warmup_line_start)[0])[
                               warmup_line_token]) * time_factor
        return driver.ExecutionResult(warmup, trials)


def lines_startswith(lines: List[str], token) -> List[str]:
    return list(filter(lambda s: s.startswith(token), lines))


def tokenize(line: str) -> List[str]:
    return list(filter(lambda x: x, line.split(' ')))


class TemporarySourcesFile:
    def __init__(self, sources: List[int]):
        self.name = f'sources_{str(time.ctime())}_.mtx'
        self.freeze = False
        self.fd = None
        self.sources = sources

    def __enter__(self):
        with open(self.name, 'wb') as sources_file:
            sources_file.write(make_sources_content(self.sources))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.freeze:
            os.remove(self.name)


def make_sources_content(sources: List[int]):
    n = len(sources)
    sources = '\n'.join(map(str, sources))

    return f'''
%%MatrixMarket matrix array real general
%-------------------------------------------------------------------------------
% Temporary sources file
%-------------------------------------------------------------------------------
{n} 1
{sources}
'''.encode('ascii')