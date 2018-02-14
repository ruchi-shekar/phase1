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

@APP.route('/scenic')
def sceniclocations() :
    """
    scenic_locations = places.get_places()
    name1=scenic_locations[0].name
    placeID1=scenic_locations[0].placeID
    rating1=scenic_locations[0].rating
    photor1=scenic_locations[0].photo

    name2=scenic_locations[1].name
    placeID2=scenic_locations[1].placeID
    rating2=scenic_locations[1].rating
    photor2=scenic_locations[1].photo

    name3=scenic_locations[2].name
    placeID3=scenic_locations[2].placeID
    rating3=scenic_locations[2].rating
    photor3=scenic_locations[2].photo
    """

    #r1 = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?type=park&location=30.267153,-97.7430608&radius=10000&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U')

    #photor1 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['results'][0]['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'


        #location2 = json1["results"][1]["formatted_address"]

    #photor2 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['results'][1]['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'


    #photor3 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['results'][2]['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'
    #    return flask.render_template('products.html', name1=name1, placeID1= placeID1, rating1=rating1, photo1=photor1, name2=name2, placeID2=placeID2, rating2=rating2, photo2=photor2, name3=name3, placeID3=placeID3, rating3=rating3, photo3=photor3)

    name1='Doug Sahm Hill Summit'
    placeID1='1'
    rating1='4.8'
    #photor1=

    name2='Scenic Overlook'
    placeID2='2'
    rating2='4.6'
    #photor2=scenic_locations[1].photo

    name3='Lou Neff Point'
    placeID3='3'
    rating3='4.7'
    #photor3=scenic_locations[2].photo

    return flask.render_template('products.html', name1=name1, placeID1= placeID1, rating1=rating1, name2=name2, placeID2=placeID2, rating2=rating2, name3=name3, placeID3=placeID3, rating3=rating3)


@APP.route('/scenic/<placeID>')
def scenicdetails(placeID):
    """
    r1 = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid=' + placeID + '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U')
    json1 = r1.json()
    name = json1['result']['name']

    address = json1["result"]["formatted_address"]
    rating = ""
    try:
        rating= json1["result"]["rating"]
    except:
        rating = "No ratings for this view yet!"
    photo = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['result']['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'
    src_for_map = "https://www.google.com/maps/embed/place?key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U&origin=place_id:" + placeID + "&output=embed"
    
    try:
        review1name = json1["result"]["reviews"][0]['author_name']
        review1text = json1["result"]["reviews"][0]['text']
        review1rating= "Rating: " + json1["result"]["reviews"][0]['rating']
        review2name = json1["result"]["reviews"][1]['author_name']
        review2text = json1["result"]["reviews"][1]['text']
        review2rating= "Rating: " + json1["result"]["reviews"][1]['rating']
    except:
        review1name = "No Reviews for this place yet!"
        review1text = ""
        review1rating=""
        review2name = ""
        review2text = ""
        review2rating=""
    
    

    scl = get_loc_from_id(placeID)s
    name = scl.name

    address = scl.address
    rating= scl.rating
    photo= scl.photo

    review1name = scl.reviews[0]['name']
    review1text = scl.reviews[0]['name']
    review1rating=scl.reviews[0]['name']
    review2name = scl.reviews[1]['name']
    review2text = scl.reviews[1]['name']
    review2rating=scl.reviews[1]['name']
    """
    if placeID is '1':
        name = 'Doug Sahm Hill Summit'
        address = 'Doug Sahm Hill Path, Austin, TX 78704'
        rating = '4.8'
        review1name = "L. Andrew Sterling"
        review1text = "Love this spot , it's elevated and you can see the whole New Austin Skyline panorama."
        review1rating= "Rating: 5"
        review2name = 'Robert Elsishans'
        review2text = 'A great spot for photos of downtown Austin.  Get to the top of the small hill and take in the scenery.  You will typically meet runners, tourists, families, and pets up on the hill.'
        review2rating= "Rating: 5"
        photo="https://photos.smugmug.com/Galleries/All/i-hbc4Wbr/4/5477538c/L/DJI_0021-cware-L.jpg"
    if placeID is '2':
        name = 'Scenic Overlook'
        address = '809, 1069 N Capital of Texas Hwy, Austin, TX 78746'
        rating = '4.6'
        review1name = "Phillip Barnhart"
        review1text = "Beautiful overlook with Austin in the distance.  Great for photographs, a good place to pull off for that phone call, or a few minutes of leg stretching.  Trash can and handicapped spot available.  We've even seen a wedding here!  A nice scenic spot."
        review1rating= "Rating: 5"
        review2name = 'Lindsay Crathers'
        review2text = 'Very nice view'
        review2rating= "Rating: 4"
        photo="https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/scenic-overlook-of-austin-mark-weaver.jpg"
    if placeID is '3':
        name = 'Lou Neff Point'
        address = 'Ann and Roy Butler Hike and Bike Trail, Austin, TX 78746'
        rating = '4.7'
        review1name = "Manni Interrupted"
        review1text = "First time here and I will say it has a beautiful view of Downtown Austin. I will definitely come to this spot again. I could only imagine the city lights at night. "
        review1rating= "Rating: 5"
        review2name = 'Jose Davila'
        review2text = ' One of the most amazing views of downtown Austin...'
        review2rating= "Rating: 5"
        photo="https://s3.amazonaws.com/gs-waymarking-images/897c10a2-3419-4794-b4c3-fc9403decb45_d.jpg"


    return flask.render_template('scenicdetails.html', name=name, address=address, photo=photo,  rating=rating, review1name=review1name, review1text=review1text, review1rating=review1rating, review2name=review2name, review2text=review2text, review2rating=review2rating)

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
