#!/usr/bin/env python
from django.core.management import execute_from_command_line
from django.db.utils import OperationalError
from argparse import ArgumentParser
from django.db import connections
from os import environ, path
from time import sleep
import logging
import re


def parse_args():
    parser = ArgumentParser()


def set_enviroments():
    environ.setdefault("DJANGO_SETTINGS_MODULE", "deutsch.settings")
    if not path.exists(".env"):
        return
    with open(".env", "r") as f:
        for l in f.readlines():
            regular = re.match(r'^.*?=', l)
            if regular:
                value = re.sub(r"^" + regular.group(0), "", l)
                environ.setdefault(
                    re.sub(r"=$", "", regular.group(0)),
                    re.sub(r"\n$", "", value)
                )


def execute_commands():
    execute_from_command_line(["deutsch", "makemigrations"])
    execute_from_command_line(["deutsch", "migrate"])
    execute_from_command_line(["deutsch", "runserver", "0.0.0.0:3000"])


def runserver():
    for _ in range(5):
        try:
            connections["default"].cursor()
            logging.info(f"connected successfuly")
            return execute_commands
        except OperationalError as e:
            logging.error(e)
        sleep(10)
    raise OperationalError


if __name__ == '__main__':
    set_enviroments()
    runserver()()
