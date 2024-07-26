from pathlib import Path

from click.testing import CliRunner
from fwheel.cli import build
from fwheel.utils.FSUtils import delete_dir, check_exists

parent_directory = Path(__file__).parent
TEST_PROJECT_PATH = parent_directory / "resources" / "ashish-libs"


def test_fwheel():
    runner = CliRunner()
    delete_dir(TEST_PROJECT_PATH / "dist", True)
    delete_dir(TEST_PROJECT_PATH / "build", True)
    result = runner.invoke(
        build, ["-p", "ashish_libs", str(TEST_PROJECT_PATH)], catch_exceptions=False
    )
    assert result.exit_code == 0
    # these directories must be created
    assert check_exists(TEST_PROJECT_PATH / "dist")
    assert check_exists(TEST_PROJECT_PATH / "build")

    # specific version must be created as well
    assert check_exists(TEST_PROJECT_PATH / "dist" / "1.0.0" / "ashish_libs-1.0.0-py3-none-any.whl", isDir=False)


def test_plibs():
    runner = CliRunner()
    result = runner.invoke(
        build, ["-p", "prophecy", "/Users/ashishpatel/prophecy-dev/prophecy-python-libs"], catch_exceptions=False
    )
    assert result.exit_code == 0

    # these directories must be created
