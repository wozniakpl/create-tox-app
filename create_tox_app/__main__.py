import argparse
import os
import sys

from create_tox_app.exit_codes import FAIL, SUCCESS
from create_tox_app.generator import Generator


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


def main():
    try:
        args = get_arguments()
        application_directory = args.appdir[0]

        if not os.path.isdir(application_directory):
            generator = Generator(application_directory)
            generator.create_application()
        else:
            print(f"Directory {application_directory} exists!")
            return FAIL

    except Exception as exception:
        print(exception)
        return FAIL
    return SUCCESS


if __name__ == "__main__":
    sys.exit(main())
