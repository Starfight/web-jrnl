#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_script import Manager
from webjrnl.controller import BP as sitebp
from webjrnl.api import BP as apibp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(sitebp)
app.register_blueprint(apibp)

# TODO: configure app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
