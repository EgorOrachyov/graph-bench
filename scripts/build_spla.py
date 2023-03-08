import subprocess
import config
import argparse
import itertools

SPLA_PATH = config.DEPS / "spla"
SPLA_BUILD = SPLA_PATH / "build"
SPLA_TARGETS = ["bfs", "sssp", "pr", "tc", "convert"]


def build(args):
    try:
        print(f"Build spla inside {SPLA_PATH} directory")
        subprocess.check_call(["cmake", str(SPLA_PATH),
                               "-B", str(SPLA_BUILD),
                               "-G", "Ninja",
                               "-DCMAKE_BUILD_TYPE=Release"])
        subprocess.check_call(["cmake", "--build", str(SPLA_BUILD)] +
                              list(itertools.chain(*[["-t", t] for t in SPLA_TARGETS])) +
                              ["-j", str(args.j)])
    except subprocess.CalledProcessError as error:
        print("Failed to build spla. Error:", error)
        return 1

    print("Done!")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--j", default=4, help="Number of threads used to build")
    args = parser.parse_args()
    return build(args)


if __name__ == '__main__':
    exit(main())
