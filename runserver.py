#!/usr/bin/env python
from django.core.management import execute_from_command_line
from os import environ, path
from argparse import ArgumentParser
import re


def parse_args():
    parser = ArgumentParser()


def set_enviroments():
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


def runserver():
    execute_from_command_line(["deutsch", "makemigrations"])
    execute_from_command_line(["deutsch", "migrate"])
    execute_from_command_line(["deutsch", "runserver", "0.0.0.0:3000"])


if __name__ == '__main__':
    set_enviroments()
    runserver()
