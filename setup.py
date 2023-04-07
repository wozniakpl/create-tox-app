from setuptools import find_packages, setup

setup(
    name="create-tox-app",
    version="1.0.1",
    url="https://github.com/wozniakpl/create-tox-app.git",
    author="Bartosz Woźniak",
    author_email="bwozniakdev@protonmail.com",
    description="A wrapper that creates a tox env with the minimal setup for a Python app.",
    long_description=open(  # noqa # pylint: disable=consider-using-with,unspecified-encoding
        "README.rst"
    ).read(),
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["create-tox-app = create_tox_app.__main__:main"]},
)
