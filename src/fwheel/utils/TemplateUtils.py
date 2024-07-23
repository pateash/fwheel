import logging

import jinja2
import pkginfo
import os

from .GenUtils import SetupPyData
from .CoreUtils import joinpath, parent_dir

TEMPLATE_FOLDER = joinpath(parent_dir(__file__), "template")


class TemplateWriter:

    def __init__(self):
        logging.debug("Creating template writer")
        template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_FOLDER)
        template_env = jinja2.Environment(loader=template_loader)
        logging.debug(f"template_env {template_env}")
        self.runner_py_template = template_env.get_template("../template/runner.py")
        logging.debug("Creating template writer1")
        self.setup_py_template = template_env.get_template("setup.txt")
        logging.debug("Creating template writer2")

        logging.debug("Creating template Done")

    def write_setup_py(self, options: SetupPyData, dest=""):
        before_setups = options.get_before_setup()
        after_setups = options.get_after_setup()
        setup_options = options.get_setup_options()
        file_path = joinpath(dest, "setup.py")
        data = self.setup_py_template.render(
            before_setups=before_setups,
            options=setup_options,
            after_setups=after_setups,
        )
        self.__write(file_path, data)

    def write_runner_py(self, dest=""):
        dest_list = []
        file_path = joinpath(dest, "deps", "runner.py")
        for i in os.scandir(os.path.join(dest, "deps")):
            dest_list.append(pkginfo.get_metadata(i.path).name)
        data = self.runner_py_template.render(dep_list=str(dest_list))
        self.__write(file_path, data)

    @staticmethod
    def __write(file_path, data):
        print(f"writing file at {file_path}")
        with open(file_path, mode="w") as s:
            s.write(data)
