#!/usr/bin/env python3

from loguru import logger
from cli.cli import cli


if __name__ == "__main__":
    logger.info("***  Pieni rukous-sovellus ***", end="\n * 2025 *")
    cli()