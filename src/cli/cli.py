import click
from utils.pdf_parser import extract_text_from_pdf


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", prompt="Your name", help="The name of the person to greet.")
def hello(name):
    click.echo(f"Hello, {name}!")


@cli.command()
def test_pdf():
    """Test PDF parsing functionality."""
    text = extract_text_from_pdf("data/jpkirja.pdf")
    word_count = sum(1 for word in text.split() if word == "Jeesus")
    click.echo(f"Sana 'Jeesus' esiintyy {word_count} kertaa")


if __name__ == "__main__":
    cli()