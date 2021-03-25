# Unit 2
pip install sphinx
sphinx-apidoc -o ./source/. ../src/
add your source files to source/index.rst
make sure when adding comments to use the correct indent
to run unittest: python -m unittest

# Unit 3

## Documentation
- Add into your `conf.py`:
```
extensions = ['sphinx.ext.autodoc',
              'recommonmark',
              'sphinx.ext.napoleon'
]
```
and
```
html_theme = 'default'
```
- Add into your `index.rst`:
```
readme
installation
license
help
modules
```
- Generate markdown files `readme.md`, `installation.md`, etc in your `doc/source` directory (the ones that are missing in the previous step)
- Fill these files with content; add further files as you see fit
- Compile your documentation on your local computer and check that it works
- Add your documentation to readthedocs
