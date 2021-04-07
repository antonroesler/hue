import click

@click.group()
def cli():
    pass

@click.option('-n', 'name')
@cli.command()
def sync(name):
    click.echo(name)

@cli.command()
def test():
    click.echo('Three')