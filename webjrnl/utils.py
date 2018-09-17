# -*- coding: utf-8 -*-
import os
from datetime import datetime

from jrnl.cli import CONFIG_PATH
from jrnl.Journal import Journal
from jrnl.util import load_and_fix_json


def convert_to_datetime(timestamp):
    """
    Convert timestamp to datetime
    :param timestamp: int
    :return: datetime
    """
    return datetime.fromtimestamp(timestamp)


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
