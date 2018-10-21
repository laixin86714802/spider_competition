#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs import app
from flask import render_template

@app.route('/video/')
@app.route('/video')
def Video():
    """任务页面"""
    return render_template('video.html')