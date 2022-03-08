import click


@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


@cli.command()
def do_something():
    """Top-level command."""


if __name__ == "__main__":
    cli()
