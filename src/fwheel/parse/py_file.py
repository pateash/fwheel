import ast

ignore_setup_options = ["install_requires"]


class SetupPyArg:
    def __init__(self, arg, value, atype, lineno, end_lineno):
        self.arg = arg
        self.value = value
        self.atype = atype
        self.lineno = lineno
        self.end_lineno = end_lineno


def parse_dict(data: ast.Dict):
    result_dict = {}
    _keys = []
    for tmp_key in data.keys:
        if isinstance(tmp_key, ast.Constant):
            _keys.append(tmp_key.value)
    for i, key_value in enumerate(data.values):
        _tmp_values = []
        for _tmp_value in key_value.elts:
            if isinstance(_tmp_value, ast.Constant):
                _tmp_values.append(_tmp_value.value)
        if _keys[i] in result_dict.keys():
            _tmp_values.extend(result_dict.get(_keys[i]))
        result_dict[_keys[i]] = _tmp_values

    return result_dict


def is_setup(node):
    return node.value.func.id == "setup"


def extract_setup_args(node):
    current_object = []
    if is_setup(node):
        current_object.append(
            SetupPyArg("before_setup", None, "from_file", 0, node.lineno)
        )
        for params in node.value.keywords:
            option = params.arg
            value = params.value
            if option not in ignore_setup_options:
                if isinstance(value, ast.Str):
                    current_object.append(
                        SetupPyArg(
                            option, value.s, "str", value.lineno, value.end_lineno
                        )
                    )
                elif isinstance(value, ast.NameConstant):
                    current_object.append(
                        SetupPyArg(
                            option, value.value, "bool", value.lineno, value.end_lineno
                        )
                    )
                elif isinstance(value, ast.Call):
                    current_object.append(
                        SetupPyArg(
                            option, value, "from_file", value.lineno, value.end_lineno
                        )
                    )
                elif isinstance(value, ast.Dict):
                    current_object.append(
                        SetupPyArg(
                            option,
                            parse_dict(value),
                            "dict",
                            value.lineno,
                            value.end_lineno,
                        )
                    )
    current_object.append(
        SetupPyArg("after_setup", None, "from_file", node.end_lineno, -1)
    )
    return current_object


def sync_setup_py(org_setup_py, new_setup_py):
    for param in new_setup_py:
        if param.atype == "from_file":
            print(param.arg)
            if param.arg == "before_setup":
                param.value = org_setup_py[param.lineno : param.end_lineno - 1]
            elif param.arg == "after_setup":
                param.value = org_setup_py[param.lineno : len(org_setup_py)]
                if len(param.value) == 0:
                    param.value.append("\n")
                else:
                    param.value[-1] = param.value[-1] + "\n"
            else:
                param.value = org_setup_py[param.lineno - 1]

    for param in new_setup_py:
        for param2 in new_setup_py:
            if param == param2:
                continue
            if param.lineno == param2.lineno:
                if param2.atype == "from_file":
                    new_setup_py.remove(param)


def get_py_file_meta_data(py_file_path):
    """api will return list of SetupPyArg"""
    with open(py_file_path, "r") as pyfile:
        setup_lines = pyfile.readlines()
        pyfile.seek(0)
        f = pyfile.read()
    node_to_traverse = ast.parse(f)
    setup_params = []

    for node in node_to_traverse.body:
        if isinstance(node, ast.Expr):
            setup_params = extract_setup_args(node)
            break

    sync_setup_py(setup_lines, setup_params)
    print(len(setup_lines))
    return setup_params
