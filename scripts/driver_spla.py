import os
import pathlib
import subprocess
import driver
import config

__all__ = [
    "DriverSpla"
]


class DriverSpla(driver.Driver):
    """
    SPLA library driver.
    Use `BENCH_DRIVER_SPLA` env variable to specify custom path to spla driver
    """

    def __init__(self):
        super().__init__()
        self.exec_dir = config.DEPS / "spla" / "build"
        self.spla_bfs = "bfs" + config.EXECUTABLE_EXT
        self.spla_sssp = "sssp" + config.EXECUTABLE_EXT
        self.spla_tc = "tc" + config.EXECUTABLE_EXT
        self.undirected = 0

        try:
            self.exec_dir = pathlib.Path(os.environ["BENCH_DRIVER_SPLA"])
            print("Set spla exec dir to:", self.exec_dir)
        except KeyError:
            pass

    def name(self) -> str:
        return "spla"

    def run_bfs(self, graph: config.Graph, source_vertex, num_iterations) -> driver.ExecutionResult:
        output = subprocess.check_output(
            [str(self.exec_dir / self.spla_bfs),
             f"--mtxpath={graph.path_original()}",
             f"--niters={num_iterations}",
             f"--source={source_vertex}",
             f"--undirected={self.undirected}"] + self._get_platform())
        return DriverSpla._parse_output(output)

    def run_sssp(self, graph: config.Graph, source_vertex, num_iterations) -> driver.ExecutionResult:
        output = subprocess.check_output(
            [str(self.exec_dir / self.spla_sssp),
             f"--mtxpath={graph.path_original()}",
             f"--niters={num_iterations}",
             f"--source={source_vertex}",
             f"--undirected={self.undirected}"] + self._get_platform())
        return DriverSpla._parse_output(output)

    def run_tc(self, graph: config.Graph, num_iterations) -> driver.ExecutionResult:
        output = subprocess.check_output(
            [str(self.exec_dir / self.spla_tc),
             f"--mtxpath={graph.path_original()}",
             f"--niters={num_iterations}"] + self._get_platform())
        return DriverSpla._parse_output(output)

    @staticmethod
    def _parse_output(output):
        lines = output.decode("ASCII").replace("\r", "").split("\n")
        runs = []
        for line in lines:
            if line.startswith("gpu(ms):"):
                runs = [float(v) for v in line.split(" ")[1:-1]]
        return driver.ExecutionResult(runs[0], runs[1:])

    def _get_platform(self):
        return [f"--platform={self.params['platform']}"]
