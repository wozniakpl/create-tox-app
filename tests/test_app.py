import sys
import tempfile
import subprocess
import os


def run(directory):
    invocation = [sys.executable, "-m", "create_tox_app", directory]
    return subprocess.run(
        invocation,
        check=False,
        text=True,
    )


def test_initializing_repo_by_name():
    with tempfile.TemporaryDirectory() as temp_dir:
        appname = "application"
        project_dir = os.path.join(temp_dir, appname)
        result = run(project_dir)
        assert result.returncode == 0
        assert os.path.isfile(os.path.join(project_dir, "setup.py"))

        application_dir = os.path.join(project_dir, appname)
        assert os.path.isdir(application_dir)
        assert os.path.isfile(os.path.join(application_dir, "__main__.py"))
        assert os.path.isfile(os.path.join(application_dir, "__init__.py"))

        tests_dir = os.path.join(project_dir, "tests")
        assert os.path.isdir(tests_dir)
        assert os.path.isfile(os.path.join(tests_dir, "test_app.py"))

        assert os.path.isfile(os.path.join(project_dir, "tox.ini"))

        assert os.path.isfile(os.path.join(project_dir, ".gitignore"))
