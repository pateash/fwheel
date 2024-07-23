import argparse

from arg_process import get_build_options
from fat import fat_builder, simple_builder
from utils import path_exits


def main():
    parser = argparse.ArgumentParser(description="Fat wheel options")
    parser.add_argument("project_dir",
                        help="project dir to build(example|project_dir=<path>|<path>|",
                        nargs=1)
    parser.add_argument("-pn", "--pkg_name",
                        help="project pkg name (example|my.utils|my)",
                        nargs=1, default=[""])
    parser.add_argument("-v", "--version",
                        help="build source dist without dependencies",
                        nargs=1, default=[""])
    parser.add_argument("-b", "--build",
                        help="build source dist without dependencies",
                        action="store_true")
    parser.add_argument("-w", "--wheel",
                        help="build wheel file without dependencies",
                        action="store_true")
    parser.add_argument("-fb", "--fat-build",
                        help="create project local copy with dependencies and build source dist",
                        action="store_true")
    parser.add_argument("-fw", "--fat-wheel",
                        help="build wheel file with all dependencies",
                        action="store_true")
    # Todo: egg is build is broken
    # parser.add_argument("-fe", "--egg",
    #                     help="build egg file with all dependencies",
    #                     action="store_true")
    parser.add_argument("-e", "--egg",
                        help="build egg file without dependencies",
                        action="store_true")
    args = parser.parse_args()
    build_options = get_build_options(args)
    project_dir = str(args.project_dir[0]).split("=")[-1]
    pkg_name = str(args.pkg_name[0]).split("=")[-1]
    version = str(args.version[0]).split("=")[-1]
    print(f"Project path: {project_dir}")
    print(f"Project pkg name: {pkg_name}")
    print(f"Fat Build options {build_options.fat}")
    print(f"Fat Build options {build_options.basic}")
    try:
        if path_exits(project_dir):
            if build_options.fat_op_present:
                fat_builder(project_dir, pkg_name, version, build_options.fat)
            if build_options.basic_op_present:
                simple_builder(project_dir, build_options.basic)
        else:
            print(f"path: {project_dir} does not exits")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
