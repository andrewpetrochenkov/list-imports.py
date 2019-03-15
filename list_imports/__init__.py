#!/usr/bin/env python
import ast
import public

@public.add
def get(path):
    """return a list of python file imports"""
    code = open(path).read()
    return parse(code)



@public.add
def parse(code):
    """return a list of python code imports"""
    imports = set()
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for subnode in node.names:
                imports.add(subnode.name)
        if isinstance(node, ast.ImportFrom):
            imports.add(node.module)
    return list(imports)
