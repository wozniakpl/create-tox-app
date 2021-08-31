import sys
import argparse
import os
from create_tox_app.exit_codes import SUCCESS, FAIL


def create_argparser():
    parser = argparse.ArgumentParser(
        description="A wrapper that creates a tox env with"
        " the minimal setup for a cli python app.",
        prog="create-tox-app",
        add_help=True,
    )
    parser.add_argument("appdir", nargs=1)

    return parser


def get_arguments():
    argparser = create_argparser()
    return argparser.parse_args()


def get_setup_py(appname):
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


def get_main_content(appname):
    return f"""import sys
from {appname}.exit_codes import SUCCESS


def main():
    print("Running {appname}")
    return SUCCESS


if __name__ == "__main__":
    sys.exit(main())
"""


def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def create_main_file(directory, appname):
    write_to_file(os.path.join(directory, "__main__.py"), get_main_content(appname))


def create_exit_codes(directory):
    write_to_file(
        os.path.join(directory, "exit_codes.py"),
        """SUCCESS = 0
FAIL = 1
""",
    )


def get_tox_ini(appname):
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


def get_gitignore():
    return """.tox
*egg-info*
*pycache*
"""


def get_test(appname):
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


def create_setup_py(appdir):
    appname = os.path.basename(appdir)
    write_to_file(os.path.join(appdir, "setup.py"), get_setup_py(appname))


def create_tox_ini(appdir):
    appname = os.path.basename(appdir)
    write_to_file(os.path.join(appdir, "tox.ini"), get_tox_ini(appname))


def create_gitignore(appdir):
    write_to_file(os.path.join(appdir, ".gitignore"), get_gitignore())


def create_test(appdir):
    appname = os.path.basename(appdir)
    write_to_file(os.path.join(appdir, "tests", "test_app.py"), get_test(appname))


def create_tests(appdir):
    os.makedirs(os.path.join(appdir, "tests"))
    create_test(appdir)


def create_implementation_dir(appdir):
    appname = os.path.basename(appdir)
    implementation_dir = os.path.join(appdir, appname)
    os.makedirs(implementation_dir)
    write_to_file(os.path.join(implementation_dir, "__init__.py"), "")
    create_main_file(implementation_dir, appname)
    create_exit_codes(implementation_dir)


def create_readme(appdir):
    appname = os.path.basename(appdir)
    write_to_file(
        os.path.join(appdir, "README.md"),
        f"""# {appname}

Install `tox` and call it in this directory.
""",
    )


def create_pylintrc(appdir):
    write_to_file(
        os.path.join(appdir, ".pylintrc"),
        """[MASTER]
disable=
    missing-class-docstring,
    missing-function-docstring,
    missing-module-docstring,
""",
    )


def main():
    args = get_arguments()

    try:
        appdir = args.appdir[0]
        if not os.path.isdir(appdir):
            os.makedirs(appdir)

            create_setup_py(appdir)
            create_implementation_dir(appdir)
            create_tox_ini(appdir)
            create_gitignore(appdir)
            create_tests(appdir)
            create_readme(appdir)
            create_pylintrc(appdir)

        else:
            print(f"Directory {appdir} exists!")
            return FAIL

    except Exception as exception:
        print(exception)
        return FAIL
    return SUCCESS


if __name__ == "__main__":
    sys.exit(main())
