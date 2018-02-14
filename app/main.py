#!/usr/bin/env python
#push initial test jaemin
from __future__ import print_function

import flask
from flask import Flask, jsonify

import githubstats


# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def home():
    return flask.render_template('home.html')

# @APP.route('/shops')
# def coffeeshops() :
#     return flask.render_template('coffeeshops.html', coffeeId1 = "1", name1 = "Summer Moon Coffee Bar", location1 = "11005 Burnet Rd Ste 112 Austin, TX 78758", price1 = "$", rating1 = "4.5", photo1 = "https://s3-media3.fl.yelpcdn.com/bphoto/WQPD9JYeDyVju0inUEID7w/o.jpg",
#                                  name2 = "Houndstooth Coffee", coffeeId2 = "2", location2 = " 401 Congress AveSte 100C Austin, TX 78701", price2 = "$$", rating2 = "4.5", photo2 = "https://s3-media3.fl.yelpcdn.com/bphoto/ITv825S32-REV1bISyfk5A/o.jpg",
#                                  name3 = "Vintage Heart Coffee", coffeeId3 = "3", location3 = "1405 E 7th St Austin, TX 78702", price3 = "$", rating3 = "4.5", photo3 = "https://s3-media3.fl.yelpcdn.com/bphoto/hK35KSh9IxFMjvvg4tCmsQ/o.jpg")

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
