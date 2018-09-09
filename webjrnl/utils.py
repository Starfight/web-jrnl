# -*- coding: utf-8 -*-
from datetime import datetime


def convert_to_datetime(timestamp):
    """
    Convert timestamp to datetime
    :param timestamp: int
    :return: datetime
    """
    return datetime.fromtimestamp(timestamp)
