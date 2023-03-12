import config
import json

DATASET_JSON = json.loads((config.METAFILES / "dataset.json").read_text())["graphs"]


class Graph:
    def __init__(self, identifier):
        self.json = next(filter(lambda d: d["source-file"] == f"{identifier}.mtx", DATASET_JSON))
        self.identifier = identifier
        self.meta_info = self.json["meta-info"]
        self.link = self.json["link"]
        self.file_name = self.json["source-file"]
        self.type = self.json["type"]
        self.dim = tuple(map(int, self.json["size"].split()[0:2]))
        self.size = int(self.json["size"].split()[2])
        self.deg_min = self.json["deg-min"]
        self.deg_max = self.json["deg-max"]
        self.deg_avg = self.json["deg-avg"]
        self.deg_sd = self.json["deg-sd"]
        self.distribution = [tuple(map(float, d.split())) for d in self.json["deg-distribution"]]

    def path_original(self):
        return config.DATASET / self.file()

    def path(self):
        return config.DATASET / f"{self.file()}{config.DATASET_SUFFIX}"

    def about(self):
        return self.id

    def file(self):
        return f"{self.id}.mtx"

    def __str__(self):
        return self.about()

    def __repr__(self):
        return self.about()

    @property
    def id(self) -> str:
        return self.identifier


ALGORITHM_NAME_bfs = "bfs"
ALGORITHM_NAME_sssp = "sssp"
ALGORITHM_NAME_pr = "pr"
ALGORITHM_NAME_tc = "tc"

GRAPH_NAME_coAuthorsCiteseer = 'coAuthorsCiteseer'
GRAPH_NAME_mycielskian19 = 'mycielskian19'
GRAPH_NAME_coPapersDBLP = 'coPapersDBLP'
GRAPH_NAME_amazon2008 = 'amazon-2008'
GRAPH_NAME_hollywood2009 = 'hollywood-2009'
GRAPH_NAME_belgium_osm = 'belgium_osm'
GRAPH_NAME_roadNetCA = 'roadNet-CA'
GRAPH_NAME_comOrkut = 'com-Orkut'
GRAPH_NAME_citPatents = 'cit-Patents'
GRAPH_NAME_rgg_n_2_22_s0 = 'rgg_n_2_22_s0'
GRAPH_NAME_socLiveJournal = 'soc-LiveJournal'
GRAPH_NAME_indochina2004 = 'indochina-2004'
GRAPH_NAME_rgg_n_2_23_s0 = 'rgg_n_2_23_s0'
GRAPH_NAME_road_central = 'road_central'
GRAPH_NAME_twitter7 = 'twitter7'

GRAPHS_NAMES_ALL = [
    GRAPH_NAME_coAuthorsCiteseer,
    GRAPH_NAME_mycielskian19,
    GRAPH_NAME_coPapersDBLP,
    GRAPH_NAME_amazon2008,
    GRAPH_NAME_hollywood2009,
    GRAPH_NAME_belgium_osm,
    GRAPH_NAME_roadNetCA,
    GRAPH_NAME_comOrkut,
    GRAPH_NAME_citPatents,
    GRAPH_NAME_rgg_n_2_22_s0,
    GRAPH_NAME_socLiveJournal,
    GRAPH_NAME_indochina2004,
    GRAPH_NAME_rgg_n_2_23_s0,
    GRAPH_NAME_road_central,
    GRAPH_NAME_twitter7
]

GRAPHS_NAMES_SHORT = {
    GRAPH_NAME_coAuthorsCiteseer: "coAutCit",
    GRAPH_NAME_mycielskian19: "myc19",
    GRAPH_NAME_coPapersDBLP: "coPapDBLP",
    GRAPH_NAME_amazon2008: "amaz2008",
    GRAPH_NAME_hollywood2009: "holl2009",
    GRAPH_NAME_belgium_osm: "belgosm",
    GRAPH_NAME_roadNetCA: "roadNetCA,",
    GRAPH_NAME_comOrkut: "comOrkut",
    GRAPH_NAME_citPatents: "citPatents",
    GRAPH_NAME_rgg_n_2_22_s0: "rggn222s0",
    GRAPH_NAME_socLiveJournal: "socLiveJour",
    GRAPH_NAME_indochina2004: "i2004",
    GRAPH_NAME_rgg_n_2_23_s0: "rggn223s0",
    GRAPH_NAME_road_central: "roadcent",
    GRAPH_NAME_twitter7: "twit7"
}

GRAPHS_NAMES_DEFAULT = [
    GRAPH_NAME_coAuthorsCiteseer,
    GRAPH_NAME_coPapersDBLP,
    GRAPH_NAME_amazon2008,
    GRAPH_NAME_hollywood2009,
    GRAPH_NAME_belgium_osm,
    GRAPH_NAME_roadNetCA,
    GRAPH_NAME_comOrkut,
    GRAPH_NAME_citPatents,
    GRAPH_NAME_rgg_n_2_22_s0,
    GRAPH_NAME_socLiveJournal,
    GRAPH_NAME_indochina2004,
    GRAPH_NAME_rgg_n_2_23_s0,
    GRAPH_NAME_road_central,
]

GRAPH_coAuthorsCiteseer = Graph(GRAPH_NAME_coAuthorsCiteseer)
GRAPH_mycielskian19 = Graph(GRAPH_NAME_mycielskian19)
GRAPH_coPapersDBLP = Graph(GRAPH_NAME_coPapersDBLP)
GRAPH_amazon2008 = Graph(GRAPH_NAME_amazon2008)
GRAPH_hollywood2009 = Graph(GRAPH_NAME_hollywood2009)
GRAPH_belgium_osm = Graph(GRAPH_NAME_belgium_osm)
GRAPH_roadNetCA = Graph(GRAPH_NAME_roadNetCA)
GRAPH_comOrkut = Graph(GRAPH_NAME_comOrkut)
GRAPH_citPatents = Graph(GRAPH_NAME_citPatents)
GRAPH_rgg_n_2_22_s0 = Graph(GRAPH_NAME_rgg_n_2_22_s0)
GRAPH_socLiveJournal = Graph(GRAPH_NAME_socLiveJournal)
GRAPH_indochina2004 = Graph(GRAPH_NAME_indochina2004)
GRAPH_rgg_n_2_23_s0 = Graph(GRAPH_NAME_rgg_n_2_23_s0)
GRAPH_road_central = Graph(GRAPH_NAME_road_central)
GRAPH_twitter7 = Graph(GRAPH_NAME_twitter7)

GRAPHS_DATA = {
    GRAPH_NAME_coAuthorsCiteseer: GRAPH_coAuthorsCiteseer,
    GRAPH_NAME_mycielskian19: GRAPH_mycielskian19,
    GRAPH_NAME_coPapersDBLP: GRAPH_coPapersDBLP,
    GRAPH_NAME_amazon2008: GRAPH_amazon2008,
    GRAPH_NAME_hollywood2009: GRAPH_hollywood2009,
    GRAPH_NAME_belgium_osm: GRAPH_belgium_osm,
    GRAPH_NAME_roadNetCA: GRAPH_roadNetCA,
    GRAPH_NAME_comOrkut: GRAPH_comOrkut,
    GRAPH_NAME_citPatents: GRAPH_citPatents,
    GRAPH_NAME_rgg_n_2_22_s0: GRAPH_rgg_n_2_22_s0,
    GRAPH_NAME_socLiveJournal: GRAPH_socLiveJournal,
    GRAPH_NAME_indochina2004: GRAPH_indochina2004,
    GRAPH_NAME_rgg_n_2_23_s0: GRAPH_rgg_n_2_23_s0,
    GRAPH_NAME_road_central: GRAPH_road_central,
    GRAPH_NAME_twitter7: GRAPH_twitter7
}

GRAPHS_BFS = [
    GRAPH_coAuthorsCiteseer,
    GRAPH_coPapersDBLP,
    GRAPH_amazon2008,
    GRAPH_hollywood2009,
    GRAPH_belgium_osm,
    GRAPH_roadNetCA,
    GRAPH_comOrkut,
    GRAPH_citPatents,
    GRAPH_rgg_n_2_22_s0,
    GRAPH_socLiveJournal,
    GRAPH_indochina2004,
    GRAPH_rgg_n_2_23_s0,
    GRAPH_road_central
]

GRAPHS_SSSP = [
    GRAPH_coAuthorsCiteseer,
    GRAPH_coPapersDBLP,
    GRAPH_amazon2008,
    GRAPH_hollywood2009,
    GRAPH_belgium_osm,
    GRAPH_roadNetCA,
    GRAPH_comOrkut,
    GRAPH_citPatents,
    GRAPH_rgg_n_2_22_s0,
    GRAPH_socLiveJournal,
    GRAPH_indochina2004,
    GRAPH_rgg_n_2_23_s0,
    GRAPH_road_central
]

GRAPHS_PR = [
    GRAPH_coAuthorsCiteseer,
    GRAPH_coPapersDBLP,
    GRAPH_amazon2008,
    GRAPH_hollywood2009,
    GRAPH_belgium_osm,
    GRAPH_roadNetCA,
    GRAPH_comOrkut,
    GRAPH_citPatents,
    GRAPH_rgg_n_2_22_s0,
    GRAPH_socLiveJournal,
    GRAPH_rgg_n_2_23_s0,
    GRAPH_road_central
]

GRAPHS_TC = [
    GRAPH_coAuthorsCiteseer,
    GRAPH_coPapersDBLP,
    GRAPH_amazon2008,
    GRAPH_roadNetCA,
    GRAPH_comOrkut,
    GRAPH_citPatents,
    GRAPH_socLiveJournal,
    GRAPH_rgg_n_2_22_s0,
    GRAPH_rgg_n_2_23_s0,
    GRAPH_road_central
]

ALGORITHMS = [
    ALGORITHM_NAME_bfs,
    ALGORITHM_NAME_sssp,
    ALGORITHM_NAME_pr,
    ALGORITHM_NAME_tc
]

GRAPHS = {
    ALGORITHM_NAME_bfs: GRAPHS_BFS,
    ALGORITHM_NAME_sssp: GRAPHS_SSSP,
    ALGORITHM_NAME_pr: GRAPHS_PR,
    ALGORITHM_NAME_tc: GRAPHS_TC
}
