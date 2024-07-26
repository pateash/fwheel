import logging
import os
import shutil
from pathlib import Path


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print(f"creating: {dir_path}")


def create_dirs(dir_path, exist_ok=True):
    print(f"creating: {dir_path}")
    os.makedirs(dir_path, exist_ok=exist_ok)


def delete_dir(dir_path, permanent=False, ignore_errors=False):
    if permanent:
        print(f"removing: {dir_path}")
        shutil.rmtree(dir_path, ignore_errors=ignore_errors)
    else:
        move(dir_path, f"trash/{dir_path.split(os.sep)[-1]}")


def check_exists(path: Path, isDir=True):
    # check if a directory exists
    if isDir:
        if path.exists() and path.is_dir():
            logging.debug(f"The directory {path} exists.")
            return True
        else:
            logging.debug(f"The directory {path} does not exist.")
            return False
    else:
        if path.exists() and path.is_file():
            logging.debug(f"The file {path} exists.")
            return True
        else:
            logging.debug(f"The file {path} does not exist.")
            return False


def move(src_dir, dst_dir):
    try:
        print(f"moving:  src = {src_dir} -> dst = {dst_dir}")
        shutil.move(src_dir, dst_dir)
    except Exception as exception:
        print(exception)
        print("Failed to move")
        print(f"SRC: {src_dir}")
        print(f"DEST: {dst_dir}")


def copy(src, dst):
    print(f"copying:  src = {src} -> dst = {dst}")
    shutil.copy2(src, dst)


def copy2(src, dst, dirs_exist_ok=False):
    print(f"copying src = {src} -> dst = {dst}")
    shutil.copytree(src, dst, dirs_exist_ok=dirs_exist_ok)
