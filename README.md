<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/list-imports.svg?maxAge=3600)](https://pypi.org/project/list-imports/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/list-imports.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/list-imports.py/actions)

### Installation
```bash
$ [sudo] pip install list-imports
```

#### Examples
```python
import list_imports
imports = list_imports.get("file.py")
```

or from string:
```python
imports = list_imports.parse(open("file.py").read())
```

cli:
```bash
$ find . -type f -name "*.py" | xargs python -m list_imports
$ find . -type f -name "*.py" | xargs python -m list_imports | awk -F"." '{print $1}'
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>