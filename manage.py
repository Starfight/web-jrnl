#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_script import Manager
from webjrnl.controller import bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(bp)

# TODO: configure app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
