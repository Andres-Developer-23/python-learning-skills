import ast


def _parse(code):
    try:
        return ast.parse(code)
    except SyntaxError:
        return None


def has_function_call(code, func_name):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == func_name:
                return True
    return False


def has_method_call(code, method_name):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == method_name:
                return True
    return False


def has_variable(code, var_name):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == var_name:
            return True
    return False


def has_if(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.IfExp)):
            return True
    return False


def has_elif(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            for child in node.orelse:
                if isinstance(child, ast.If):
                    return True
    return False


def has_else(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.If) and node.orelse:
            has_nested_if = any(isinstance(n, ast.If) for n in node.orelse)
            if not has_nested_if and len(node.orelse) > 0:
                return True
    return False


def has_for(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.AsyncFor)):
            return True
    return False


def has_while(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            return True
    return False


def has_return(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            return True
    return False


def has_fstring(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):
            return True
    return False


def has_list_literal(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.List):
            return True
    return False


def has_dict_or_set(code):
    tree = _parse(code)
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, (ast.Dict, ast.Set)):
            return True
    return False


def count_function_defs(code):
    tree = _parse(code)
    if tree is None:
        return 0
    return sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
