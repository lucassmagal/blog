#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, send_file

DEBUG = False

app = Flask(__name__, static_folder='build/static')
app.config.from_object(__name__)


# @app.route('/')
# def index():
#     return send_file('build/index.html', cache_timeout=60)


@app.route('/<path:path>/')
def application(path):
    path = "build/%s/index.html" % path
    return send_file(path, cache_timeout=60)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
