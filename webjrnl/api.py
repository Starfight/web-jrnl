# -*- coding: utf-8 -*-
import os
from datetime import datetime
from flask import Blueprint, jsonify
from flask_restful import Api, Resource, abort
from jrnl.cli import CONFIG_PATH
from jrnl.Journal import Journal
from jrnl.util import load_and_fix_json
from webjrnl.utils import convert_to_datetime

BP = Blueprint('api', __name__, url_prefix='/api')
API = Api(BP)


@API.resource("/entries",
              "/entries/<int:timestamp_start>/<int:timestamp_end>")
class EntriesApi(Resource):
    def get(self, timestamp_start=None, timestamp_end=None):
        # parse date
        date_start = datetime.now().replace(hour=0,
                                            second=0,
                                            minute=0,
                                            microsecond=0)
        date_end = date_start.replace(hour=23,
                                      second=59,
                                      minute=59,
                                      microsecond=999999)
        try:
            if timestamp_start:
                date_start = convert_to_datetime(timestamp_start)
            if timestamp_end:
                date_end = convert_to_datetime(timestamp_end)
        except ValueError as e:
            abort(422, message="Error: %s" % str(e))
        # open journal
        config = load_and_fix_json(CONFIG_PATH)
        default_path = config['journals'].get('default')
        config['journal'] = os.path.expanduser(os.path.expandvars(default_path))
        default_journal = Journal('default', **config)
        # search entries
        default_journal.filter(start_date=date_start.isoformat(),
                               end_date=date_end.isoformat())
        return jsonify({
            "entries": [x.to_dict() for x in default_journal.entries]
        })
