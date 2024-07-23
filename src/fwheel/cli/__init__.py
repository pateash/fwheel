import logging

import click

from .info import info
from ..__about__ import __version__
from ..utils.BuildUtils import get_build_options
from ..utils.CliUtils import check_update
from ..utils.CoreUtils import path_exits
from ..utils.FatUtils import fat_builder, simple_builder
from ..utils.MessageUtils import warning

LOGGING_LEVELS = {
    0: logging.NOTSET,
    # 1: logging.ERROR,
    # 2: logging.WARN,
    1: logging.INFO,
    2: logging.DEBUG,
}  #: a mapping of `verbose` option counts to logging levels


# Define a format for the console handler
class Info:
    """An information object to pass data between CLI functions."""

    def __init__(self):  # Note: This object must have an empty constructor.
        """Create a new instance."""
        self.verbose: int = 0


# pass_info is a decorator for functions that pass 'Info' objects.
pass_info = click.make_pass_decorator(Info, ensure=True)


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.option(
    "--verbose",
    "-v",
    count=True,
    help="Enable verbose output, use -v for INFO and -vv for DEBUG",
)
@click.version_option(version=__version__, prog_name="hckr")
@click.pass_context
@pass_info
def cli(
    _info: Info,
    ctx: click.Context,
    verbose: int,
):
    if verbose > 0:
        logging.basicConfig(
            level=(LOGGING_LEVELS.get(verbose, logging.DEBUG)),
            format="[%(levelname)s]: %(message)s",
        )
        warning(
            f"Verbose logging (LEVEL={'INFO' if verbose == 1 else 'DEBUG'}) is enabled. "
            "Use -v for INFO, -vv for DEBUG logs"
        )
    _info.verbose = verbose
    if ctx.invoked_subcommand is None:
        click.secho("hckr ", fg="magenta", bold=True, nl=False)
        click.secho(f"v{__version__}  ", fg="blue", bold=True, nl=False)
        click.secho(
            f"https://github.com/hckr-cli/hckr\n", fg="green", bold=True, nl=False
        )
        check_update()
        cli(["-h"])
    else:
        check_update()


@click.command()
@click.argument("project_dir")
@click.option(
    "-p", "--pkg-name", default="", help="project pkg name (example|my.utils|my)"
)
@click.option(
    "-v", "--version", default="", help="build source dist without dependencies"
)
@click.option(
    "-b", "--build", is_flag=True, help="build source dist without dependencies"
)
@click.option(
    "-w", "--wheel", is_flag=True, help="build wheel file without dependencies"
)
@click.option(
    "-fb",
    "--fat-build",
    is_flag=True,
    help="create project local copy with dependencies and build source dist",
)
@click.option(
    "-fw", "--fat-wheel", is_flag=True, help="build wheel file with all dependencies"
)
@click.option("-e", "--egg", is_flag=True, help="build egg file without dependencies")
def build(project_dir, pkg_name, version, build, wheel, fat_build, fat_wheel, egg):
    """This command build fat wheel for project"""
    build_options = get_build_options(wheel, egg, build, fat_wheel, fat_build)
    print(f"Project path: {project_dir}")
    print(f"Project pkg name: {pkg_name}")
    print(f"Fat Build options {build_options.fat}")
    print(f"Fat Build options {build_options.basic}")
    try:
        if path_exits(project_dir):
            logging.debug(f"project_dir {project_dir} exists")
            if build_options.fat_op_present:
                logging.debug(
                    f"build_options.fat_op_present {build_options.fat_op_present} exists"
                )
                fat_builder(project_dir, pkg_name, version, build_options.fat)
            if build_options.basic_op_present:
                logging.debug(
                    f"build_options.basic_op_present {build_options.basic_op_present} exists"
                )
                simple_builder(project_dir, build_options.basic)
        else:
            print(f"path: {project_dir} does not exist")
    except Exception as e:
        print(e)


cli.add_command(build)

if __name__ == "__main__":
    cli()
