#!/usr/bin/env python3
from django.core.management import execute_from_command_line
from django.db.utils import OperationalError
from argparse import ArgumentParser
from django.db import connections
from dotenv import load_dotenv
from os import environ
from time import sleep
import logging


def parse_args():
    parser = ArgumentParser()


def execute_commands():
    execute_from_command_line([__name__, "makemigrations"])
    execute_from_command_line([__name__, "migrate"])

    HOST = environ.get("HOST", "0.0.0.0")
    PORT = environ.get("PORT", "3000")
    execute_from_command_line([__name__, "runserver", f"{HOST}:{PORT}"])


def runserver():
    for try_count in range(1, 6):
        try:
            connections["default"].cursor()
            logging.info(f"connected successfuly")
            return execute_commands
        except OperationalError as e:
            x = connections["default"].settings_dict
            error = (
                f"{try_count} try: {e.args[1]} credentials - {x['USER']}:{x['PASSWORD']}"
                if len(e.args) > 1 else e
            )
            logging.error(error)
        sleep(10)
    raise OperationalError


if __name__ == '__main__':
    load_dotenv()
    load_dotenv("config.env")
    runserver()()
