#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs import app
from flask import render_template

@app.route('/graph/')
@app.route('/graph')
def Groph():
    """关系页面"""
    return render_template('graph.html')