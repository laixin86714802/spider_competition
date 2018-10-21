#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs import app
from flask import render_template

@app.route('/word/')
@app.route('/word')
def Word():
    """词频统计"""
    return render_template('word.html')

