import os
from typing import List

INSTALL_PKG_IN_DIR_CMD = "python -m pip install -r requirements.txt -t ."
DOWNLOAD_WHEEL_CMD = "python -m pip download -r requirements.txt --dest {deps} --no-cache"
FAT_WHEEL_INSTALL = "python -m pip download -r requirements.txt --dest deps --no-cache"
BUILD_CMD = "python setup.py {build_options}"
INSTALL_LOCAL_PKG_CMD = "python -m pip install --no-index --find-links=deps -r requirements.txt"


def download_wheel(path):
    _execute(DOWNLOAD_WHEEL_CMD.format(deps=os.path.join(path, "deps")))


def fat_wheel_install():
    _execute(FAT_WHEEL_INSTALL)


def install():
    _execute(BUILD_CMD.format(build_options="install"))


def build(options: List[str]):
    build_option_str = " ".join(options)
    _execute(BUILD_CMD.format(build_options=build_option_str))


def _execute(cmd):
    dir_path = f"~{os.path.basename(os.getcwd())}"
    print(f"{dir_path}> {cmd}")
    os.system(cmd)
