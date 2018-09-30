# -*- coding: utf-8 -*-
import os
from datetime import datetime
from flask import Blueprint, jsonify
from flask_restful import Api, Resource, abort, reqparse
from webjrnl.utils import convert_to_datetime, get_journal

BP = Blueprint('api', __name__, url_prefix='/api')
API = Api(BP)


@API.resource("/entries")
class EntriesApi(Resource):
    def get(self):
        # parse date
        parser = reqparse.RequestParser()
        parser.add_argument('date_start',
                            default=datetime.now().replace(hour=0,
                                                           second=0,
                                                           minute=0,
                                                           microsecond=0),
                            location='args',
                            type=convert_to_datetime,
                            help='Date cannot be converted')
        parser.add_argument('date_end',
                            default=datetime.now().replace(hour=23,
                                                           second=59,
                                                           minute=59,
                                                           microsecond=999999),
                            location='args',
                            type=convert_to_datetime,
                            help='Date cannot be converted')
        args = parser.parse_args()

        # open journal
        default_journal = get_journal('default')
        # search entries
        default_journal.filter(start_date=args['date_start'].isoformat(),
                               end_date=args['date_end'].isoformat())
        return jsonify({
            "entries": [x.to_dict() for x in default_journal.entries]
        })
