import abc
import statistics
import dataset
import dataclasses
import typing


@dataclasses.dataclass
class ExecutionResult:
    """
    Result of the execution of the single algorithm benchmark run
    """
    warm_up: float
    times: typing.List[float]

    def avg(self):
        return statistics.mean(self.times)

    def median(self):
        return statistics.median(self.times)

    def sd(self):
        return statistics.stdev(self.times)

    def maximum(self):
        return max(self.times)

    def minimum(self):
        return min(self.times)

    def brief_str(self) -> str:
        return f'warm_up={self.warm_up:.2f}ms, avg={self.avg():.2f}ms, ' \
               f'sd={self.sd():.2f}, median={self.median():.2f}ms, ' \
               f'min={self.minimum()}ms, max={self.maximum()}ms'

    def __str__(self) -> str:
        return self.brief_str()

    def __repr__(self) -> str:
        return self.brief_str()


class Driver:
    """
    Base class for any driver, which is responsible for running
    algorithm benchmarks for third-party tools from stand-alone
    executable files.

    Algorithms:
        * bfs         (breadth-first search)
        * sssp        (single-source shortest paths)
        * pr          (page rank)
        * tc          (triangles counting)
        * [future] cc (connected components)
    """

    def __init__(self):
        self.params = dict()
        self.graph_exceptions = dict()

    @abc.abstractmethod
    def name(self) -> str:
        """
        Retrieve driver name
        :return: Driver name
        """
        pass

    @abc.abstractmethod
    def run_bfs(self, graph: dataset.Graph, source_vertex: int, num_iterations: int) -> ExecutionResult:
        """
        Run bfs algorithm benchmark.
        :param graph: Graph with its properties to run on
        :param source_vertex: Source vertex to start algorithm
        :param num_iterations: Number of iteration to run
        :return: execution results
        """
        pass

    @abc.abstractmethod
    def run_sssp(self, graph: dataset.Graph, source_vertex: int, num_iterations: int) -> ExecutionResult:
        """
        Run sssp algorithm benchmark.
        :param graph: Graph with its properties to run on
        :param source_vertex: Source vertex to start algorithm
        :param num_iterations: Number of iteration to run
        :return: execution results
        """
        pass

    @abc.abstractmethod
    def run_pr(self, graph: dataset.Graph, num_iterations: int) -> ExecutionResult:
        """
        Run pr algorithm benchmark.
        :param graph: Graph with its properties to run on
        :param num_iterations: Number of iteration to run
        :return: execution results
        """
        pass

    @abc.abstractmethod
    def run_tc(self, graph: dataset.Graph, num_iterations: int) -> ExecutionResult:
        """
        Run tc algorithm benchmark.
        :param graph: Graph with its properties to run on
        :param num_iterations: Number of iteration to run
        :return: execution results
        """
        pass

    def run(self, graph: dataset.Graph, algo: str, params: dict) -> ExecutionResult:
        """
        Execute driver benchmark with specified params
        :param graph: Graph to analyse
        :param algo: Algorithm name to run
        :param params: Additional params
        :return: execution result
        """
        self.params = params

        if algo == 'bfs':
            result = self.run_bfs(graph, int(params['source']), int(params['num_iterations']))
        elif algo == 'sssp':
            result = self.run_sssp(graph, int(params['source']), int(params['num_iterations']))
        elif algo == 'pr':
            result = self.run_pr(graph, int(params['num_iterations']))
        elif algo == 'tc':
            result = self.run_tc(graph, int(params['num_iterations']))
        else:
            raise Exception(f"Unknown algorithm {algo}")

        return result

    def exceptions(self):
        return self.graph_exceptions

    def __str__(self):
        return self.name()

    def __repr__(self):
        return self.name()
