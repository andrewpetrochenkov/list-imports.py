#!/usr/bin/env python
import ast
import public


@public.add
def get(string):
    """return a list of imports"""
    imports = set()
    tree = ast.parse(string)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for subnode in node.names:
                imports.add(subnode.name)
        if isinstance(node, ast.ImportFrom):
            imports.add(node.module)
    return list(imports)
