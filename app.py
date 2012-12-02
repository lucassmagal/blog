#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


def _key(page):
    n = page.meta['published'].toordinal()
    if 'order' in page.meta:
        n += int(page.meta['order'])

    return n


def _posts(pages):
    posts = (p for p in pages if 'published' in p.meta)
    return sorted(posts, reverse=True, key=lambda p: _key(p))


@freezer.register_generator
def post():
    posts = (p for p in pages if 'published' in p.meta)
    for post in posts:
        yield {'title': post['slug']}


@app.route('/')
def index():
    posts = _posts(pages)
    return render_template('index.html', post=posts[0], posts=posts[1:10])


@app.route('/post/<string:title>/')
def post(title):
    post = pages.get_or_404(title)
    return render_template('post.html', post=post)


@app.route('/arquivo/')
def arquivo():
    return render_template('arquivo.html', posts=_posts(pages))


@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')


@app.route('/atom.xml/')
def atom_feed():
    posts = _posts(pages)
    return render_template('atom.xml', update_date=posts[0]['published'],
                           posts=posts)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(port=8000)
