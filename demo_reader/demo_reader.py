import click
import pluggy

import hookspec
from plugins import YAMLPlugin, JSONPlugin, CsvPlugin


def get_plugin_manager():
    pm = pluggy.PluginManager('demo_reader')
    pm.add_hookspecs(hookspec)
    pm.register(YAMLPlugin())
    pm.register(JSONPlugin())
    pm.register(CsvPlugin())
    return pm


@click.group()
def cli():
    pass


@click.command()
@click.option('--path', '-p', required=True, type=click.Path(exists=True))
@click.option('--noop')
def read(path, **kwargs):
    """
    Read file input

    Example:
        python demo_reader/demo_reader.py read -p test.yml
    """
    pm = get_plugin_manager()
    data = pm.hook.demo_reader_read_data(path=path, config=kwargs)

    # hook call returns a single result because we added `firstresult=True`
    # to the hookspec
    print(data)


cli.add_command(read)


if __name__ == "__main__":
    cli()