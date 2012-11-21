#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_DESTINATION = 'output/build'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@freezer.register_generator
def post():
    posts = (p for p in pages if 'published' in p.meta)
    for post in posts:
        yield {'title': post['slug']}


@app.route('/')
def index():
    posts = (p for p in pages if 'published' in p.meta)
    latest = sorted(posts, reverse=True,
                    key=lambda p: p.meta['published'])
    return render_template('index.html', posts=latest[:10])


@app.route('/post/<string:title>/')
def post(title):
    post = pages.get_or_404(title)
    return render_template('post.html', post=post)


@app.route('/arquivo/')
def arquivo():
    posts = (p for p in pages if 'published' in p.meta)
    posts = sorted(posts, reverse=True,
                   key=lambda p: p.meta['published'])
    return render_template('arquivo.html', posts=posts)


@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(port=8000)
