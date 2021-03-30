from pathlib import Path
import yaml

from pluggy import HookimplMarker


hookimpl = HookimplMarker("demo_reader")


class YAMLPlugin:
    """A hook implementation namespace for YAML."""

    @hookimpl
    def read_data(path, config):
        """Read YAML input"""
        if Path(path).suffix in ('yaml', 'yml'):
            return yaml.safe_load(Path(path).read_text())
