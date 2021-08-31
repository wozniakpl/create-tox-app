def t_main(appname):
    return f"""import sys
from {appname}.exit_codes import SUCCESS


def main():
    print("Running {appname}")
    return SUCCESS


if __name__ == "__main__":
    sys.exit(main())
"""


def t_setup_py(appname):
    return f"""from setuptools import setup, find_packages

setup(
    name="{appname}",
    version="1.0.0",
    url="https://github.com/something_like_{appname}.git",
    author="AUTHOR",
    author_email="MAIL",
    description="DESCRIPTION",
    packages=find_packages(),
    install_requires=[],
    entry_points={{
        "console_scripts": [
            "{appname} = {appname.replace("-", "_")}.__main__:main",
        ]
    }},
)
"""


def t_tox_ini(appname):
    return f"""[tox]
envlist = py38, check_format, lint

[testenv]
deps =
    pytest
commands =
    pytest {{posargs}}

[testenv:check_format]
deps =
    black
commands =
    black --check {appname} tests setup.py

[testenv:lint]
deps =
    pylint
    flake8
commands =
    pylint {appname} tests setup.py
    flake8 {appname} tests setup.py
"""


def t_gitignore():
    return """.tox
*egg-info*
*pycache*
"""


def t_test(appname):
    return f"""import sys
import subprocess


def run():
    args = []
    invocation = [sys.executable, "-m", "{appname}", *args]
    return subprocess.run(
        invocation,
        check=False,
        text=True,
    )


def test_app():
    result = run()
    assert result.returncode == 0
"""


def t_exit_codes():
    return """SUCCESS = 0
FAIL = 1
"""


def t_pylintrc():
    return """[MASTER]
disable=
    missing-class-docstring,
    missing-function-docstring,
    missing-module-docstring,
"""


def t_readme(appname):
    return f"""# {appname}

Install `tox` and call it in this directory.
"""
