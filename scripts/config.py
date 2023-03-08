import pathlib
import platform

ROOT = pathlib.Path(__file__).parent.parent
DATASET = ROOT / "dataset"
DEPS = ROOT / "deps"

SYSTEM = {'Darwin': 'macos', 'Linux': 'linux', 'Windows': 'windows'}[platform.system()]
EXECUTABLE_EXT = {'macos': '', 'windows': '.exe', 'linux': ''}[SYSTEM]
LIBRARY_EXT = {'macos': '.dylib', 'linux': '.so', 'windows': '.dll'}[SYSTEM]
DATASET_SUFFIX = ".conv"

DEFAULT_NUM_ITERATIONS = 10
DEFAULT_SOURCE_VERTEX = 0
