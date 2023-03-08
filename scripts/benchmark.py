import config
import dataset
import driver_graphblast
import driver_gunrock
import driver_lagraph
import driver_spla
import argparse
import stats

DRIVERS = {
    "graphblast": driver_graphblast.DriverGraphBLAST(),
    "gunrock": driver_gunrock.DriverGunrock(),
    "lagraph": driver_lagraph.DriverLaGraph(),
    "spla": driver_spla.DriverSpla()
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", default="all", help="Algorithm to test [all, bfs, sssp, pr, tc]")
    parser.add_argument("--tool", default="all", help="Tool to test [all, graphblast, gunrock, lagraph, spla]")
    parser.add_argument("--num-iterations", default=10, help="Number of iteration to run each test")
    parser.add_argument("--source", default=config.DEFAULT_SOURCE_VERTEX, help="Source vertex for bfs, sssp, etc.")
    parser.add_argument("--graph", help="Graph to run algorithms")
    parser.add_argument("--platform", default="0", help="OpenCL platform to run (for OpenCL-based tools)")
    parser.add_argument("--csv", default="benchmark.cvs", help="Csv table to save benchmark results")
    args = parser.parse_args()

    if args.algo == 'all':
        algos = dataset.ALGORITHMS
    else:
        algos = args.algo.split(",")

    if args.tool == 'all':
        tools = list(DRIVERS.values())
    else:
        tools = list(map(lambda x: DRIVERS[x], args.tool.split(",")))

    if args.graph is None:
        graphs = dataset.GRAPHS
    else:
        graphs = {algo: [dataset.GRAPHS_DATA[args.graph]] for algo in algos}

    params = {
        "num_iterations": int(args.num_iterations),
        "source": int(args.source),
        "platform": str(args.platform)
    }

    print("Run benchmarks:")
    print(f" algos: {repr(algos)}")
    print(f" tools: {repr(tools)}")
    print(f" graphs: {repr(graphs)}")
    print(f" params: {repr(params)}")

    run_stats = dict()

    for algorithm in algos:
        print(f"Execute: {algorithm}")
        algo_stats = run_stats[algorithm] = dict()
        for tool in tools:
            print(f" Tool: {tool}")
            tool_stats = algo_stats[tool.name()] = dict()
            for g in graphs[algorithm]:
                print(f"  Graph: {g}")
                try:
                    # skip some graphs
                    if algorithm in tool.exceptions() and g.id in tool.exceptions()[algorithm]:
                        print(f"  Skip: {g}")
                        continue

                    res = tool_stats[g.id] = tool.run(g, algorithm, params)
                    print(f"  Result: {res}")
                except Exception as e:
                    print(f"  Failed due {e}")

    stats.output_stats(run_stats)
    stats.output_stats_csv(run_stats, args.csv)


if __name__ == '__main__':
    main()
