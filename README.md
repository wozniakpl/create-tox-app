# create-tox-app

A small script to set up a tox environment with `setup.py`, formatting, linting and tests.

It does this:
```
$ create-tox-app my_app_name
$ tree -a my_app_name/
my_app_name/
├── .gitignore
├── .pylintrc
├── README.md
├── my_app_name
│   ├── __init__.py
│   ├── __main__.py
│   └── exit_codes.py
├── setup.py
├── tests
│   └── test_app.py
└── tox.ini
```

You're ready to call `tox` to run tests, format check and linting. `tox -e format` would reformat your code. 
# Installation

```
pip3 install git+https://github.com/wozniakpl/create-tox-app.git
```