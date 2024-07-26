from pathlib import Path

from click.testing import CliRunner
from fwheel.cli import build

parent_directory = Path(__file__).parent
TEST_PROJECT_PATH = parent_directory / "resources" / "ashish-libs"


def test_fwheel():
    runner = CliRunner()
    print("\n", TEST_PROJECT_PATH)
    result = runner.invoke(
        build, ["-p", "ashish_libs", str(TEST_PROJECT_PATH)], catch_exceptions=False
    )
    print(result.output)
