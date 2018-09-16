# -*- coding: utf-8 -*-
from flask import render_template, Blueprint

BP = Blueprint('index', __name__)


@BP.route("/")
def index():
    return render_template('index.html')
