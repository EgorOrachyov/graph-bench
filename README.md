# graph-bench

[![JB Research](https://jb.gg/badges/research-flat-square.svg)](https://research.jetbrains.org/)
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

| Name              | Vertices |     Edges | Max Degree |                                                                                                                             Download |
|:------------------|---------:|----------:|-----------:|-------------------------------------------------------------------------------------------------------------------------------------:|
| coAuthorsCiteseer |   227.3K |      1.6M |       1372 |                                    [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coAuthorsCiteseer.tar.gz) |
| mycielskian19     |   393.2K | 903194.7M |     196607 |                                                                               [link](http://sparse.tamu.edu/Mycielski/mycielskian19) |
| coPapersDBLP      |   540.4K |     30.4M |       3299 |                                         [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coPapersDBLP.tar.gz) |
| amazon-2008       |   735.3K |      5.2M |       1086 |                                                                                       [link](http://sparse.tamu.edu/LAW/amazon-2008) |
| hollywood-2009    |     1.1M |    113.8M |      11467 |                                            [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/hollywood-2009.tar.gz) |
| belgium_osm       |     1.4M |      3.1M |         10 |                                                                                  [link](http://sparse.tamu.edu/DIMACS10/belgium_osm) |
| roadNet-CA        |     1.9M |      5.5M |         12 |                                               [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/roadNet-CA.tar.gz) |
| com-Orcut         |       3M |      234M |      33313 |                                                [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/com-Orkut.tar.gz) |
| cit-Patents       |     3.7M |     16.5M |        793 |                                              [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/cit-Patents.tar.gz) |
| rgg_n_2_22_s0     |     4.1M |     60.7M |         36 |                                        [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/rgg_n_2_22_s0.tar.gz) |
| soc-LiveJournal   |     4.8M |     68.9M |      20333 |                                         [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/soc-LiveJournal1.tar.gz) |
| indochina-2004    |     7.5M |    194.1M |     256425 |                                            [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/indochina-2004.tar.gz) |
| rgg_n_2_23_s0     |     8.3M |    127.0M |         40 |                                        [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/rgg_n_2_23_s0.tar.gz) |
| road_central      |    14.1M |     33.8M |          8 |                                                                                 [link](http://sparse.tamu.edu/DIMACS10/road_central) |
| twitter7          |    41.6M |      1.4B |      3.08M |                                                                                         [link](http://sparse.tamu.edu/SNAP/twitter7) |

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

Run particular tool for performance measurements.

```shell
python3 scripts/benchmark.py --tool=[all, spla, lagraph, gunrock, graphblast]
```

Run particular algorithm for performance measurements.

```shell
python3 scripts/benchmark.py --algo=[all, bfs, sssp, pr, tc]
```

See help for more options.

```shell
python3 scripts/benchmark.py -h
```

## License

This project licensed under MIT License. License text can be found in the
[license file](./LICENSE.md).

## Acknowledgments <img align="right" width="15%" src="https://github.com/EgorOrachyov/graph-bench/raw/main/docs/jetbrains-logo.png?raw=true&sanitize=true">

This is a research project of the Programming Languages and Tools Laboratory
at JetBrains-Research. Laboratory website [link](https://research.jetbrains.org/groups/plt_lab/).