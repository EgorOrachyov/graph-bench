import subprocess

import config

SPLA = config.DEPS / "spla"
SPLA_BUILD = SPLA / "build"
SPLA_DATA_TOOL = SPLA_BUILD / "convert"


def main():
    print("Convert graphs:")
    for graph in config.GRAPHS_DATA.values():
        subprocess.call([str(SPLA_DATA_TOOL),
                         f"--in={graph.path_original()}",
                         f"--out={graph.path()}"])
        print(f" Output graph to {graph.path()}")


if __name__ == '__main__':
    main()
