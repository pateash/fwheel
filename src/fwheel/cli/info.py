import logging
import time
import webbrowser

import click

from ..__about__ import __version__
from ..utils.CliUtils import check_update
from ..utils.MessageUtils import error


@click.group(
    help="info commands",
    context_settings={"help_option_names": ["-h", "--help"]},
)
def info():
    pass


@info.command()
def version():
    """
    Show information for CLI and useful links.

    **Example usage**:

    .. code-block:: shell

        $ hckr info version
        Version: hckr==VERSION
        Github: https://github.com/pateash/fwheel
        PyPi: https://pypi.org/project/fwheel/

    **Command Reference**:
    """
    click.secho("Version: fwheel", fg="magenta", bold=True, nl=False)
    click.secho(f"=={__version__}  ", fg="blue", bold=False, nl=True)
    check_update(show_no_update=True)
    click.secho(
        f"Github: https://github.com/pateash/fwheel", fg="red", bold=True, nl=True
    )
    click.secho(
        f"PyPi: https://pypi.org/project/fwheel/", fg="yellow", bold=True, nl=True
    )


@info.command(help="Opens docs for fwheel in browser")
def docs():
    url = "https://fwheel.readthedocs.io/"
    click.secho("Version: fwheel", fg="yellow", bold=True, nl=False)
    click.secho(f"=={__version__}  ", fg="blue", bold=False, nl=True)
    click.secho(f"Opening Docs in browser: {url}", fg="red", bold=True, nl=True)
    time.sleep(1)
    try:
        webbrowser.open(url)
    except Exception as e:
        error(f"Some error occured while opening docs in browser\n{e}")
