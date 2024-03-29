# graph-bench

[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/JetBrains-Research/spla-bench/blob/master/LICENSE.md)

Benchmarks suite for performance study of various graph analysis frameworks for CPU/GPU computations.

## Tools description

| Name       | Brief                                                              | Platform | Technology |                                        Source Page |
|:-----------|:-------------------------------------------------------------------|---------:|-----------:|---------------------------------------------------:|
| Spla       | Generalized linear sparse linear algebra for multi-GPU computation |      GPU |     OpenCL | [link](https://github.com/JetBrains-Research/spla) |
| GraphBLAST | High-performance linear algebra-based graph primitives on GPUs     |      GPU |       CUDA |      [link](https://github.com/gunrock/graphblast) |
| Gunrock    | High-performance graph primitives on GPUs                          |      GPU |       CUDA |         [link](https://github.com/gunrock/gunrock) |
| LaGraph    | Collection of graph algorithms for SuiteSparse:GraphBLAS libray    |      CPU |     OpenMP |       [link](https://github.com/GraphBLAS/LAGraph) |

## Dataset description

| Name              | Vertices |   Edges | Avg Deg | Sd Deg | Min Deg |   Max Deg |                                                                                              Link |
|:------------------|---------:|--------:|--------:|-------:|--------:|----------:|--------------------------------------------------------------------------------------------------:|
| coAuthorsCiteseer |   227.3K |    1.6M |     7.2 |   10.6 |     0.0 |    1372.0 | [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coAuthorsCiteseer.tar.gz) |
| mycielskian19     |   393.2K |  903.2M |  2296.4 | 3950.8 |     0.0 |  196606.0 |                                            [link](http://sparse.tamu.edu/Mycielski/mycielskian19) |
| coPapersDBLP      |   540.5K |   30.5M |    56.4 |   66.2 |     0.0 |    3299.0 |      [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coPapersDBLP.tar.gz) |
| amazon-2008       |   735.3K |    7.0M |     9.6 |    7.6 |     0.0 |    1077.0 |                                                    [link](http://sparse.tamu.edu/LAW/amazon-2008) |
| hollywood-2009    |     1.1M |  112.8M |    98.9 |  271.9 |     0.0 |   11467.0 |         [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/hollywood-2009.tar.gz) |
| belgium_osm       |     1.4M |    3.1M |     2.2 |    0.5 |     0.0 |      10.0 |                                               [link](http://sparse.tamu.edu/DIMACS10/belgium_osm) |
| roadNet-CA        |     2.0M |    5.5M |     2.8 |    1.0 |     0.0 |      12.0 |            [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/roadNet-CA.tar.gz) |
| com-Orkut         |     3.1M |  234.4M |    76.3 |  154.8 |     0.0 |   33313.0 |             [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/com-Orkut.tar.gz) |
| cit-Patents       |     3.8M |   33.0M |     8.8 |   10.5 |     0.0 |     793.0 |           [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/cit-Patents.tar.gz) |
| rgg_n_2_22_s0     |     4.2M |   60.7M |    14.5 |    3.8 |     0.0 |      36.0 |     [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/rgg_n_2_22_s0.tar.gz) |
| soc-LiveJournal   |     4.8M |   85.7M |    17.7 |   52.0 |     0.0 |   20333.0 |      [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/soc-LiveJournal1.tar.gz) |
| indochina-2004    |     7.4M |  302.0M |    40.7 |  329.6 |     0.0 |  256425.0 |         [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/indochina-2004.tar.gz) |
| rgg_n_2_23_s0     |     8.4M |  127.0M |    15.1 |    3.9 |     0.0 |      40.0 |     [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/rgg_n_2_23_s0.tar.gz) |
| road_central      |    14.1M |   33.9M |     2.4 |    0.9 |     0.0 |       8.0 |                                              [link](http://sparse.tamu.edu/DIMACS10/road_central) |
| twitter7          |    41.7M | 2405.0M |    57.7 |  401.5 |     0.0 | 2997490.0 |                                                      [link](http://sparse.tamu.edu/SNAP/twitter7) |

## Instructions

### 1. How to get source code

Download benchmark repository source code.

```shell
git clone https://github.com/EgorOrachyov/graph-bench.git
```

Within repo folder init git submodule to get all source code of tools.

```shell
git submodule update --init --recursive
```

### 2. How to build tools

#### 2.1 Spla

Build bundled Spla library.

```shell
python3 scripts/build_spla.py
```

#### 2.2 Gunrock

Build bundled Gunrock library.

```shell
python3 scripts/build_gunrock.py
```

#### 2.3 GraphBLAST

Build bundled GraphBLAST library.

```shell
python3 scripts/build_graphblast.py
```

#### 2.4 LaGraph

Build bundled SuiteSparse and LaGraph libraries.

```shell
python3 scripts/build_lagraph.py
```

### 3. How to download data

Download all graphs one by one archives and extract into [dataset](./dataset) folder.
Alternatively, download all graphs within single archive
from [Google Drive](https://drive.google.com/file/d/14RHaC_Ze_qoeb2GuhXOkirVaTvkRlv35/view?usp=share_link).

### 5. How to prepare data

After dataset unpack into [dataset](./dataset) folder you have to run convert tool to prepare graphs.

```shell
python3 scripts/convert.py
```

This tool uses spla `convert.exe` to convert source `.mtx` files into undirected `.mtx` graphs.

### 6. How to run benchmarks

Run all algorithms & graphs & tools performance measurements.

```shell
python3 scripts/benchmark.py
```

Run particular tool for performance measurements. Use comma and no space to select multiple.

```shell
python3 scripts/benchmark.py --tool=[all, spla, lagraph, gunrock, graphblast]
```

```shell
python3 scripts/benchmark.py --tool=spla,lagraph,gunrock,graphblast
```

Run particular algorithm for performance measurements. Use comma and no space to select multiple.

```shell
python3 scripts/benchmark.py --algo=[all, bfs, sssp, pr, tc]
```

```shell
python3 scripts/benchmark.py --algo=bfs,sssp,pr,tc
```

Provide csv file name to save all stats of the benchmark.

```shell
python3 scripts/benchmark.py --csvall=my_results.csv
```

Provide csv file name to save per-tool detailed stats of the benchmark.

```shell
python3 scripts/benchmark.py --csvtool=my_results.csv
```

See help for more options.

```shell
python3 scripts/benchmark.py -h
```

## License

This project licensed under MIT License. License text can be found in the
[license file](./LICENSE.md).