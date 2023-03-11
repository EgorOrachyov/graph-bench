import subprocess
import config
import dataset
import argparse

SPLA = config.DEPS / "spla"
SPLA_BUILD = SPLA / "build"
SPLA_DATA_TOOL = SPLA_BUILD / "convert"


def main(statsonly):
    print("Convert graphs:")
    for graph in dataset.GRAPHS_DATA.values():
        subprocess.call([str(SPLA_DATA_TOOL),
                         f"--in={graph.path_original()}",
                         f"--out={graph.path()}",
                         f"--stats_only={statsonly}"])
        print(f" Output graph to {graph.path()}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--statsonly", default=False, help="save only graph stats dropping data")
    args = parser.parse_args()
    main(args.statsonly)
