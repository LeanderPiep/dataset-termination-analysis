import importlib.util
import sys

spec = importlib.util.spec_from_file_location("module", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

args = [int(x) for x in sys.argv[2:]]

module.main(*args)