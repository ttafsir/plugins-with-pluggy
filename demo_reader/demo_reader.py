import click


def get_plugin_manager():
    pass


@click.group()
def cli():
    pass


@click.command()
@click.option('--path', '-p', required=True, type=click.Path(exists=True))
@click.option('-noop')
def read(path, **kwargs):
    pass


cli.add_command(read)