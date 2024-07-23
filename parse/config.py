import os
from fat_wheel.parse import yaml
from fat_wheel.utils import parent_dir


def get_include_files(config_yaml):
    config_dict = yaml.read(file_name=config_yaml)
    include_file_folder = config_dict.get("include")
    return include_file_folder


def get_ignore_files(path):
    ignore_files = []
    if path is not None:
        include_file_folder = get_include_files(path)
        for file_folder in os.scandir(parent_dir(path)):
            if file_folder.name not in include_file_folder:
                ignore_files.append(file_folder.name)
    else:
        ignore_files = ["venv", "src", ".idea", "build", ".git", "dist", ".gitignore", "test"]
    return ignore_files


def get_pkg_name(path):
    config_dict = yaml.read(file_name=path)
    pkg_name = config_dict.get("pkg_name")
    return pkg_name
