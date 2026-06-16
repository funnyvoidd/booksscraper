import importlib

def load_parser(name):
    return importlib.import_module(f"src.parsers.{name}").parse


def load_exporter(name):
    return importlib.import_module(f"src.exporters.{name}").export