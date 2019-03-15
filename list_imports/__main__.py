#!/usr/bin/env python
"""list a python file(s) imports"""
import click
import list_imports
import os
import sys

MODULE_NAME = "list_imports"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME


@click.command()
@click.argument('paths', nargs=-1,required=False)
def _cli(paths):
    imports = []
    for path in paths:
        imports+= list(list_imports.get(path))
    imports = list(set(imports))
    if imports:
        print("\n".join(sorted(imports)))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
