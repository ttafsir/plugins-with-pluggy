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
            return yaml.safe_load(Path(path).read_text())
