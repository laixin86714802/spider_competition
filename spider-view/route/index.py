#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs import app
from flask import render_template

@app.route('/index/')
@app.route('/index')
def Index():
    """首页"""
    return render_template('index.html')