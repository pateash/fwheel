from pathlib import Path

from click.testing import CliRunner

from fwheel.cli import build
from fwheel.__about__ import __version__

parent_directory = Path(__file__).parent
TEST_PROJECT_PATH = parent_directory / "resources" / "ashish-libs"


def test_fwheel():
    runner = CliRunner()
    result = runner.invoke(build, ["-p", TEST_PROJECT_PATH])
    print(result.output)
    assert result.exit_code == 0
    assert __version__ in result.output
    assert "[OPTIONS] COMMAND [ARGS]..." in result.output
    assert (
        """Options:
  -v, --verbose  Enable verbose output, use -v for INFO and -vv for DEBUG
  --version      Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  cron    cron commands
  crypto  crypto commands
  data    data related commands
  hash    hash commands
  info    info commands
  k8s     Kubernetes commands
  repl    Start an interactive shell"""
        in result.output
    )
