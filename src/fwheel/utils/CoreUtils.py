from datetime import datetime
import os
import io

CURRENT_DATE = datetime.now()
YEAR = CURRENT_DATE.year
MONTH = CURRENT_DATE.month
DAY = CURRENT_DATE.day
PATH_SEPARATOR = os.sep


def extract_deps(config):
    """read deps from reqirements.txt"""
    with io.open(config, "r", encoding="utf-8") as c:
        deps = c.read().splitlines()
    return list(
        map(lambda x: x.split("=")[0].lower(), filter(lambda x: len(x) != 1, deps))
    )


def now(date_format="%Y-%m-%d-%H-%M-%S"):
    return datetime.now().strftime(date_format)


def path_exits(path):
    return os.path.exists(path)


def isdir(path):
    return os.path.isdir(path)


def scandir(path):
    return os.scandir(path)


def chdir(path):
    os.chdir(path)


def parent_dir(path):
    return os.path.dirname(path)


def parent_dir_name(path):
    return os.path.basename(path)


def joinpath(*args, **kwargs):
    return os.path.join(*args, **kwargs)


def getcwd():
    return os.getcwd()


def getabspath(path):
    return os.path.abspath(path)


def is_pkg(root_dir, pkg_name):
    nested_pkg_list = pkg_name.split(".")
    for i, nested_pkg in enumerate(nested_pkg_list):
        nested_pkg_path = joinpath(
            root_dir, PATH_SEPARATOR.join(nested_pkg_list[0 : i + 1]), "__init__.py"
        )
        if not path_exits(nested_pkg_path):
            return False
    return True
