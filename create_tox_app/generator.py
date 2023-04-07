import os

from create_tox_app.templates import (
    t_exit_codes,
    t_gitignore,
    t_main,
    t_pylintrc,
    t_readme,
    t_setup_py,
    t_test,
    t_tox_ini,
)


def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


class Generator:
    def __init__(self, directory):
        self.application_directory = directory
        self.application_name = os.path.basename(self.application_directory)
        self.implementation_dir = os.path.join(
            self.application_directory, self.application_name
        )

    def create_setup_py(self):
        write_to_file(
            os.path.join(self.application_directory, "setup.py"),
            t_setup_py(self.application_name),
        )

    def create_main_file(self):
        write_to_file(
            os.path.join(self.implementation_dir, "__main__.py"),
            t_main(self.application_name),
        )

    def create_exit_codes(self):
        write_to_file(
            os.path.join(self.implementation_dir, "exit_codes.py"),
            t_exit_codes(),
        )

    def create_implementation_dir(self):
        os.makedirs(self.implementation_dir)
        write_to_file(os.path.join(self.implementation_dir, "__init__.py"), "")
        self.create_main_file()
        self.create_exit_codes()

    def create_tox_ini(self):
        write_to_file(
            os.path.join(self.application_directory, "tox.ini"),
            t_tox_ini(self.application_name),
        )

    def create_gitignore(self):
        write_to_file(
            os.path.join(self.application_directory, ".gitignore"), t_gitignore()
        )

    def create_test(self):
        write_to_file(
            os.path.join(self.application_directory, "tests", "test_app.py"),
            t_test(self.application_name),
        )

    def create_tests(self):
        os.makedirs(os.path.join(self.application_directory, "tests"))
        self.create_test()

    def create_readme(self):
        write_to_file(
            os.path.join(self.application_directory, "README.md"),
            t_readme(self.application_name),
        )

    def create_pylintrc(self):
        write_to_file(
            os.path.join(self.application_directory, ".pylintrc"), t_pylintrc()
        )

    def create_application(self):
        os.makedirs(self.application_directory)

        self.create_setup_py()
        self.create_implementation_dir()
        self.create_tox_ini()
        self.create_gitignore()
        self.create_tests()
        self.create_readme()
        self.create_pylintrc()
