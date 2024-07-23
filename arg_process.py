from enum import Enum
from typing import NamedTuple, List


class BuildType(str, Enum):
    WHEEL = "bdist_wheel"
    EGG = "bdist_egg"
    SDIST = "sdist"
    BUILD = "build"


class BuildOption(NamedTuple):
    fat: List[BuildType]
    basic: List[BuildType]
    basic_op_present: bool
    fat_op_present: bool


def get_build_options(args):
    fat_options = []
    basic_options = []
    if args.wheel:
        basic_options.append(BuildType.WHEEL)
    if args.egg:
        basic_options.append(BuildType.EGG)
    if args.build:
        basic_options.append(BuildType.BUILD)
        basic_options.append(BuildType.SDIST)

    if args.fat_wheel:
        fat_options.append(BuildType.WHEEL)
    # if args.fat_egg:
    #     fat_options.append(BuildType.EGG)
    if args.fat_build:
        fat_options.append(BuildType.BUILD)
        fat_options.append(BuildType.SDIST)

    basic_op_present = len(basic_options) != 0
    fat_op_present = len(fat_options) != 0

    if not fat_op_present and not basic_op_present:
        fat_options.append(BuildType.WHEEL)
        fat_op_present = True

    return BuildOption(fat_options, basic_options, basic_op_present, fat_op_present)
