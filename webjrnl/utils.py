# -*- coding: utf-8 -*-
import os
from datetime import datetime

from jrnl.cli import CONFIG_PATH
from jrnl.Journal import Journal
from jrnl.util import load_and_fix_json


def convert_to_datetime(isodate):
    """
    Convert timestamp to datetime
    :param isodate: str date ISO-8601
    :return: datetime
    """
    return datetime.strptime(isodate, "%Y-%m-%dT%H:%M:%S")


def get_journal(name):
    """
    Return Journal with name
    :param name: string
    :return: Journal
    """
    config = load_and_fix_json(CONFIG_PATH)
    default_path = config['journals'].get(name)
    config['journal'] = os.path.expanduser(os.path.expandvars(default_path))
    return Journal(name, **config)
