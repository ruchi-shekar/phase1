#!/usr/bin/env python
#push initial test jaemin
from __future__ import print_function

import flask
from flask import Flask, jsonify

import githubstats


# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def hello():
    return "hello world"

@APP.route('/home')
def home():
    return flask.render_template('home.html')

# @APP.route('/coffeeshops')
# def home():
#     return flask.render_template('coffeshops.html')

# @APP.route('/scenic')
# def home():
#     return flask.render_template('products.html')

# @APP.route('/snapshots')
# def home():
#     return flask.render_template('snapshotsmain.html')

@APP.route('/about')
def about():
    commits = githubstats.user_commits()
    issues = githubstats.user_issues()
    return flask.render_template('about.html', total_commits = commits["total"], issues = githubstats.open_issues + issues["total"], amrutha_commits = commits["amrutha"], sonam_commits = commits["sonam"],
                                 jenni_commits = commits["jenni"], ruchi_commits = commits["ruchi"], jaemin_commits = commits["jaemin"], amrutha_issues = issues["amrutha"],
                                 sonam_issues = issues["sonam"], jenni_issues = issues["jenni"], ruchi_issues = issues["ruchi"], jaemin_issues = issues["jaemin"])



if __name__ == '__main__':
    #APP.debug=True
    APP.run()
