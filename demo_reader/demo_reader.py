import click
import pluggy

import hookspec
from plugins import YAMLPlugin


def get_plugin_manager():
    pm = pluggy.PluginManager('demo_reader')
    pm.add_hookspecs(hookspec)
    pm.register(YAMLPlugin())
    return pm


@click.group()
def cli():
    pass


@click.command()
@click.option('--path', '-p', required=True, type=click.Path(exists=True))
@click.option('--noop')
def read(path, **kwargs):
    pm = get_plugin_manager()
    data = pm.hook.demo_reader_read_data(path=path, config=kwargs)
    print(data)


cli.add_command(read)


if __name__ == "__main__":
    cli()