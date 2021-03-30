import csv
import json
from pathlib import Path

import yaml

from pluggy import HookimplMarker


hookimpl = HookimplMarker("demo_reader")


class YAMLPlugin:
    """A hook implementation namespace for YAML."""

    @hookimpl
    def demo_reader_read_data(self, path, config):
        """Read YAML input"""
        print(f'attempting YAML plugin for input {path}...')
        if Path(path).suffix in ('.yaml', '.yml'):
            print('=> processing YAML input...')
            return yaml.safe_load(Path(path).read_text())


class JSONPlugin:
    """A hook implementation namespace for JSON."""

    @hookimpl
    def demo_reader_read_data(self, path, config):
        """Read JSON input"""
        print(f'attempting JSON plugin for input {path}...')
        if Path(path).suffix == '.json':
            print('=> processing JSON input...')
            return json.loads(Path(path).read_text())


class CsvPlugin:
    """A hook implementation namespace for Csv."""

    @hookimpl
    def demo_reader_read_data(self, path, config):
        """Read Csv input"""
        print(f'attempting CSV plugin for input {path}...')
        if Path(path).suffix == '.csv':
            print('=> processing CSV input...')
            csv_reader = csv.DictReader(Path(path).open())
            return [row for row in csv_reader]