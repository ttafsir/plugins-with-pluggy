from pluggy import HookspecMarker

hookspec = HookspecMarker("demo_reader")


@hookspec
def demo_reader_read_data(path, config):
    """
    read data from different formats

    :param path: Path object to read data from
    :type path: str
    :param config: config dictionary to plugin implementations
    :type config: dict
    """