"""Command line interface for prayer of the moment."""

from loguru import logger
import click
from src.utils.pdf_parser import extract_text_from_pdf, get_sisallys

@click.group()
def cli():
    """Command line interface for prayer of the moment."""
    pass


@cli.command()
@click.option("--name", prompt="Your name", help="The name of the person to greet.")
def hello(name):
    """Greet a person."""
    click.echo(f"Hello, {name}!")


@cli.command()
def test_pdf():
    """Test PDF parsing functionality."""
    text = extract_text_from_pdf("data/jpkirja.pdf")
    word_count = sum(1 for word in text.split() if word == "Jeesus")
    click.echo(f"Sana 'Jeesus' esiintyy {word_count} kertaa")


def get_logo() -> None:
    app_name = "Prayer of the Moment"
    banner = f" ### {app_name} ### "
    logger.info(banner)
    

def cli() -> None:
    get_logo()
    while True:
        if input("Press q to quit: ") == "q":
            break
        elif input("[1] Hae sisältö") == "1":
            sisallys = get_sisallys("data/jpkirja.pdf")
            if sisallys:
                logger.info(f"Sisällys: {sisallys}")
            else:
                logger.error("Sisällys ei löytynyt")
        else:
            logger.error("Invalid input")




if __name__ == "__main__":
    cli()