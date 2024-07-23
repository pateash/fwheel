from .ProjectUtils import Project
from .CoreUtils import now, joinpath, scandir, chdir, isdir
from .FSUtils import copy, copy2, create_dirs
from .GenUtils import SetupPyData
from .TemplateUtils import TemplateWriter
from ..cmd.pip import download_wheel, build
from ..parse.config import get_ignore_files
import logging

DIST = "dist"
BUILD = "build"


def move_dist(project):
    dst = joinpath(project.root_dir, DIST, project.version)
    copy2(src=DIST, dst=dst, dirs_exist_ok=True)


def fat_builder(project_dir, pkg_name, version, options):
    logging.debug("Fat Builder called")
    writer = TemplateWriter()
    project = Project.build(project_dir, pkg_name, version)
    setup_py_data = SetupPyData.build_setup_py_meta_data(
        project.root_dir, project.pkg_name, project.version
    )
    project.set_version(version=setup_py_data.get_version())
    logging.debug(f"Project info {project}")
    print(project)
    fat_wheel_build = f"{project.name}-v{project.version}-{now()}"
    fat_wheel_build_path = joinpath(project.root_dir, BUILD, fat_wheel_build)
    create_dirs(fat_wheel_build_path)
    ignored_files = get_ignore_files(project.get_fat_wheel_yaml_path())
    print(f"Ignored files/folder: {ignored_files}")
    required_files = list(scandir(project.root_dir))
    print(f"creating project local copy in build/{fat_wheel_build}")
    for file in required_files:
        if file.name not in ignored_files:
            print(file.path)
            if isdir(file.path):
                dst = joinpath(fat_wheel_build_path, file.name)
                copy2(src=file.path, dst=dst)
            else:
                copy(src=file.path, dst=fat_wheel_build_path)

    print(f"chdir: {fat_wheel_build_path}")
    chdir(fat_wheel_build_path)
    download_wheel(project.get_pkg_path())
    writer.write_runner_py(dest=project.get_pkg_path())
    writer.write_setup_py(setup_py_data, dest=fat_wheel_build_path)
    with open(joinpath(project.get_pkg_path(), "deps", "__init__.py"), mode="w") as f:
        f.write("")
    build(options)
    move_dist(project)


def simple_builder(project_dir, options):
    logging.debug("Simple Builder called")
    if Project.is_root_dir(project_dir):
        chdir(project_dir)
        build(options)
