import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", prompt="Your name", help="The name of the person to greet.")
def hello(name):
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    cli()
