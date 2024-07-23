from enum import Enum

from .CoreUtils import (
    joinpath,
    path_exits,
    PATH_SEPARATOR,
    getcwd,
    getabspath,
    parent_dir_name,
    extract_deps,
    is_pkg,
)


class ProjectConfigs(Enum):
    REQUIREMENTS_TXT = "requirements.txt"
    FAT_WHEEL_YAML = "fat-wheel.yaml"
    PY_PROJECT_YAML = "pyproject.toml"
    SETUP_PY = "setup.py"


class ProjectConfigPath:

    def __init__(self, root_dir):
        self.setup_py_path = joinpath(root_dir, ProjectConfigs.SETUP_PY.value)
        self.fat_wheel_yaml_path = joinpath(
            root_dir, ProjectConfigs.FAT_WHEEL_YAML.value
        )
        self.py_project_yaml_path = joinpath(
            root_dir, ProjectConfigs.PY_PROJECT_YAML.value
        )
        self.requirements_txt_path = joinpath(
            root_dir, ProjectConfigs.REQUIREMENTS_TXT.value
        )

    def setup_py_exists(self):
        return path_exits(self.setup_py_path)

    def requirements_txt_exists(self):
        return path_exits(self.requirements_txt_path)

    def fat_wheel_yaml_exists(self):
        return path_exits(self.fat_wheel_yaml_path)

    def py_project_yaml_exists(self):
        return path_exits(self.py_project_yaml_path)

    def __repr__(self):
        return str(self.__dict__)


class Project:

    def __init__(self, name, version, pkg_name, root_dir, deps, project_config_path):
        self.name = name
        self.version = version
        self.root_dir = root_dir
        self.deps = deps
        self.pkg_name = pkg_name
        self.project_config_path: ProjectConfigPath = project_config_path

    @classmethod
    def build(cls, root_dir, pkg_name, version):
        if root_dir.strip().__eq__(""):
            root_dir = getcwd()
        root_dir = getabspath(root_dir)
        name = parent_dir_name(root_dir)
        project_config_path = ProjectConfigPath(root_dir)
        if not is_pkg(root_dir, pkg_name):
            raise Exception(f"please provide valid --pkg_name arguments")
        if not project_config_path.requirements_txt_exists():
            raise Exception("requirements.txt not found")
        deps = extract_deps(project_config_path.requirements_txt_path)
        return cls(name, version, pkg_name, root_dir, deps, project_config_path)

    @staticmethod
    def is_root_dir(path):
        project_config_path = ProjectConfigPath(path)
        return project_config_path.requirements_txt_exists()

    def build_strategy(self):
        build_by_setup_py = self.project_config_path.setup_py_exists()
        build_by_pyproject_toml = self.project_config_path.py_project_yaml_exists()
        if not build_by_setup_py and not build_by_pyproject_toml:
            raise Exception("either setup.py or pyproject.toml should exists")

    def set_version(self, version):
        if self.version is None or self.version == "":
            self.version = version

    def get_version(self):
        return self.version

    def get_setup_py_path(self):
        return self.project_config_path.setup_py_path

    def get_fat_wheel_yaml_path(self):
        return self.project_config_path.fat_wheel_yaml_path

    def get_requirements_txt_path(self):
        return self.project_config_path.requirements_txt_path

    def get_py_project_yaml_path(self):
        return self.project_config_path.py_project_yaml_path

    def get_pkg_path(self):
        return self.pkg_name.replace(".", PATH_SEPARATOR)

    def __repr__(self):
        return str(self.__dict__)
