import os
from fat_wheel.parse.py_file import get_py_file_meta_data, SetupPyArg


class SetupPyData:

    def __init__(self):
        self.version = None
        self.before_setup = None
        self.after_setup = None
        self.setup_options = None

    @staticmethod
    def build_setup_py_meta_data(root_dir, pkg_name, version):
        setup_py_data = SetupPyData()
        meta_data = get_py_file_meta_data(os.path.join(root_dir, "setup.py"))
        default_include_package_data = True
        default_package_data = True
        default_entry_points = True
        default_find_package = True
        project_name = None
        for meta in meta_data:
            if meta.arg == "name":
                project_name = meta.value
            if meta.arg == "version":
                if version is None or version == "":
                    version = meta.value
                meta.value = version
            elif meta.arg == "package_data":
                default_package_data = False
                package_data_dict = meta.value
                pkg_data = ["*"]
                if pkg_name in package_data_dict:
                    pkg_data.extend(package_data_dict.get(pkg_name))
                package_data_dict[f"{pkg_name}.deps"] = pkg_data
            elif meta.arg == "entry_points":
                default_entry_points = False
                entry_points_list = meta.value.get("console_scripts")
                entry_points = [f"install-{project_name} = {pkg_name}.deps.runner:install"]
                entry_points_list.extend(entry_points)
            elif meta.arg == "packages":
                default_find_package = False
            elif meta.arg == "include_package_data":
                meta.value = True
                default_include_package_data = False

        if default_find_package:
            packages = SetupPyArg("packages", "\tpackages=find_packages()", "from_file", 0, 0)
            meta_data.insert(-1, packages)

        if default_entry_points:
            entry_points_dict = {"console_scripts": [f"install-{project_name} = {pkg_name}.deps.runner:install"]}
            entry_points = SetupPyArg("entry_points", entry_points_dict, "dict", 0, 0)
            meta_data.insert(-1, entry_points)

        if default_package_data:
            package_data_dict = {f"{pkg_name}.deps": ["*"]}
            package_data = SetupPyArg("package_data", package_data_dict, "dict", 0, 0)
            meta_data.insert(-1, package_data)

        if default_include_package_data:
            include_package_data = SetupPyArg("include_package_data", "\tinclude_package_data=True", "from_file", 0, 0)
            meta_data.insert(-1, include_package_data)

        for m in meta_data:
            if m.arg == "before_setup" or m.arg == "after_setup":
                tmp = []
                for g in m.value:
                    if g != "\n":
                        tmp.append(g[:-1])
                m.value = tmp

        setup_py_data.version = version
        setup_py_data.before_setup = meta_data.pop(0)
        setup_py_data.after_setup = meta_data.pop(-1)
        setup_py_data.setup_options = meta_data
        return setup_py_data

    def get_version(self):
        return self.version

    def get_before_setup(self):
        return self.before_setup

    def get_after_setup(self):
        return self.after_setup

    def get_setup_options(self):
        return self.setup_options
