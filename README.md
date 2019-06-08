<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/list-imports.svg?longCache=True)](https://pypi.org/project/list-imports/)
[![](https://img.shields.io/pypi/v/list-imports.svg?maxAge=3600)](https://pypi.org/project/list-imports/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/list-imports.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/list-imports.py/)

#### Installation
```bash
$ [sudo] pip install list-imports
```

#### Functions
function|`__doc__`
-|-
`list_imports.get(path)` |return a list of python file imports
`list_imports.parse(code)` |return a list of python code imports

#### Executable modules
usage|`__doc__`
-|-
`python -m list_imports path ...` |list a python file(s) imports

#### Examples
```python
import list_imports
imports = list_imports.get(open("file.py").read())
```

```bash
$ find . -type f -name "*.py" | xargs python -m list_imports
$ find . -type f -name "*.py" | xargs python -m list_imports | awk -F"." '{print $1}'
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>