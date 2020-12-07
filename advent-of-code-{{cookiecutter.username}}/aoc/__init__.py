import importlib
import sys


def solution(year, day, data):
    mod_name = "aoc.aoc{}.q{:02d}".format(year, day)
    importlib.import_module(mod_name)
    return sys.modules[mod_name].solution(data)
