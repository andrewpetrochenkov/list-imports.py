#!/usr/bin/env python
import list_imports
import os

path = os.__file__
imports = list_imports.get(path)
print(imports)
