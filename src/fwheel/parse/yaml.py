import yaml


def writer(*args, **kwargs):
    file_name = kwargs.get("file_name")
    data = kwargs.get("data")
    mode = "w" if kwargs.get("mode") is None or kwargs.get("mode") not in ["a", "w"] else kwargs.get("mode")
    with open(file_name, mode=mode) as yml_file:
        yaml.dump(data, yml_file)


def read(*args, **kwargs):
    file_name = kwargs.get("file_name")
    with open(file_name, mode="r") as yml_file:
        test = yaml.full_load(yml_file)
    return test
