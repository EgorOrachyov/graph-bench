import pathlib
import platform

from dataclasses import dataclass

ROOT = pathlib.Path(__file__).parent.parent
DATASET = ROOT / "dataset"
DEPS = ROOT / "deps"

SYSTEM = {'Darwin': 'macos', 'Linux': 'linux', 'Windows': 'windows'}[platform.system()]
EXECUTABLE_EXT = {'macos': '', 'windows': '.exe', 'linux': ''}[SYSTEM]
LIBRARY_EXT = {'macos': '.dylib', 'linux': '.so', 'windows': '.dll'}[SYSTEM]
DATASET_SUFFIX = ".dt.un.rl"

DEFAULT_NUM_ITERATIONS = 10
DEFAULT_SOURCE_VERTEX = 0

GRAPHS_NAMES = [
    'coAuthorsCiteseer',
    'coPapersDBLP',
    'amazon-2008',
    'hollywood-2009',
    'belgium_osm',
    'roadNet-CA',
    'com-Orkut',
    'cit-Patents',
    'rgg_n_2_22_s0',
    'soc-LiveJournal',
    'indochina-2004',
    'rgg_n_2_23_s0',
    'road_central'
]


@dataclass
class Graph:
    id: str

    def path_original(self):
        return DATASET / f"{self.id}.mtx"

    def path(self):
        return DATASET / f"{self.id}.mtx{DATASET_SUFFIX}"

    def about(self):
        return self.id

    def __str__(self):
        return self.about()

    def __repr__(self):
        return self.about()


GRAPHS_DATA = {name: Graph(name) for name in GRAPHS_NAMES}

GRAPHS_BFS = [
    GRAPHS_DATA['amazon-2008'],
    GRAPHS_DATA['hollywood-2009'],
    GRAPHS_DATA['belgium_osm'],
    GRAPHS_DATA['roadNet-CA'],
    GRAPHS_DATA['com-Orkut'],
    GRAPHS_DATA['cit-Patents'],
    GRAPHS_DATA['soc-LiveJournal'],
    GRAPHS_DATA['indochina-2004'],
    GRAPHS_DATA['rgg_n_2_22_s0'],
    GRAPHS_DATA['rgg_n_2_23_s0'],
    GRAPHS_DATA['road_central']
]

GRAPHS_SSSP = [
    GRAPHS_DATA['amazon-2008'],
    GRAPHS_DATA['hollywood-2009'],
    GRAPHS_DATA['belgium_osm'],
    GRAPHS_DATA['roadNet-CA'],
    GRAPHS_DATA['com-Orkut'],
    GRAPHS_DATA['cit-Patents'],
    GRAPHS_DATA['soc-LiveJournal'],
    GRAPHS_DATA['indochina-2004'],
    GRAPHS_DATA['rgg_n_2_22_s0'],
    GRAPHS_DATA['rgg_n_2_23_s0'],
    GRAPHS_DATA['road_central']
]

GRAPHS_TC = [
    GRAPHS_DATA['coAuthorsCiteseer'],
    GRAPHS_DATA['coPapersDBLP'],
    GRAPHS_DATA['roadNet-CA'],
    GRAPHS_DATA['com-Orkut'],
    GRAPHS_DATA['cit-Patents'],
    GRAPHS_DATA['soc-LiveJournal'],
    GRAPHS_DATA['rgg_n_2_22_s0'],
    GRAPHS_DATA['rgg_n_2_23_s0']
]

ALGORITHMS = ["bfs", "sssp", "tc"]
GRAPHS = {"bfs": GRAPHS_BFS, "sssp": GRAPHS_SSSP, "tc": GRAPHS_TC}
