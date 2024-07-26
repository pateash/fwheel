import os

INSTALL_LOCAL_PKG_CMD = "python -m pip install --no-index --find-links={deps} -r {req}"

DEP_NAME_LIST = {{dep_list}}


def install():
    deps_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "deps")
    print(deps_path)
    for DEP_NAME in DEP_NAME_LIST:
        print("*" * 100)
        print(f"installing {DEP_NAME}")
        os.system(
            f"python -m pip install --no-index --find-links={deps_path} {DEP_NAME}"
        )
    import shutil

    print(shutil.which("python"))


if __name__ == "__main__":
    install()
