from sys import flags
from typing import Pattern, Text
from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
import json
from bson import ObjectId
import re
from datetime import datetime
import random
import re
# from Crypto.Hash import HMAC, SHA256# from Crypto.Cipher import AES
import bcrypt
import unicodedata
import smtplib
from pymongo.message import query
# from twilio.rest import Client
from bson import json_util
# import boto3
from werkzeug.utils import secure_filename
# import key_config as keys

client = pymongo.MongoClient("mongodb+srv://test:test123@cluster0.ebfkx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.swipeup

import hashlib, uuid


# connection_url = 'mongodb+srv://admin:samplearticle@cluster0-pm5vp.mongodb.net/test?retryWrites=true&w=majority'
app = Flask(__name__)
# client = pymongo.MongoClient(connection_url)
  

# s3 = boto3.client('s3',
#                     aws_access_key_id='access key here',
#                     aws_secret_access_key= 'secret key here',
#                     aws_session_token='secret token here'
#                      )
# BUCKET_NAME='hackershrine'



# Database
# Database = client.get_database('Example')
# # Table
# SampleTable = Database.SampleTable
collection = db['profile']
collections = db['videos']
videocall = db["videocalls"]
bookmarks = db['bookmarks']
postt=db['post']
registartion = db['registration']
follower_request = db['followers_request']
follower_table = db['follower']
otp = db['Otp']
chat_db = db['chat']
# app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# @app.route('/find/', methods=['GET'])
# def findAll():
#     query = collection.find()
#     output = {}
#     abc = [] #array
#     i = 0
#     print('***')
#     print(query)
#     print('***')
#     for x in query:
#         abc.append(x)
#         # output[i] = x
#         # output[i].pop('_id')
#         # i += 1
#         print(x)
#     print(abc)
#     output["users"] = abc
#     # output["users"].pop('_id')

#     return JSONEncoder().encode(output)
#     # return jsonify(output)



@app.route('/find/', methods=['GET'])
def findAllsss():
    query = collection.find()
    output = {}
    abc = [] #array
    i = 0
    print('***')
    print(query)
    print('***')
    for x in query:
        abc.append(x)
        # output[i] = x
        # output[i].pop('_id')
        # i += 1
        print(x)
    print('***')
    print(abc)
    print('***')
    output["users"] = abc
    # output["users"].pop('_id')

    return JSONEncoder().encode(output)
    # return jsonify(output)

#################### error ##########################
@app.route('/findfriends', methods=['POST'])
def findAlls():
    values = request.values.get("username") 
    print(len(values))
    # if len(values) == 0:
    #     output = {}
    #     print('*')
    # else:
    v1 = '.*'+values+'.*'
    rgx = re.compile(v1, re.IGNORECASE)
    print(rgx)
    queryObject = {"username": rgx}
    query = collection.find(queryObject)
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["users"] = abc
    return JSONEncoder().encode(output)


# @app.route('/findfriends', methods=['POST'])
# def findAlls():
#     values = request.values.get("username") 
#     print(len(values))
#     # if len(values) == 0:
#     #     output = {}
#     #     print('*')
#     # else:
#     v1 = '.*'+values+'.*'
#     rgx = re.compile(v1, re.IGNORECASE)
#     print(rgx)
#     queryObject = {"username": rgx}
#     query = collection.find(queryObject)
#     output = {}
#     abc = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x)
#         print(x)
#     print(abc)
#     output["users"] = abc
#     return JSONEncoder().encode(output)



#################### error #########################
@app.route('/searchtabs', methods=['POST'])
def findAllss():
    values = request.values.get("search") 
    print(len(values))
    if len(values) == 0:
        output = {}
        print('*')
    else:
        v1 = '.*'+values+'.*'
        rgx = re.compile(v1, re.IGNORECASE)
        print(rgx)
        queryObject = {"username": rgx}
        query = collection.find(queryObject)
        output = {}
        abc = []
        i = 0
        print(query)
        for x in query:
            abc.append(x)
            print(x)
        print(abc)
        output["users"] = abc
    return JSONEncoder().encode(output)



@app.route('/follow', methods=['POST'])
def follow():
    follower_id = request.values.get("follower_id") 
    following_id = request.values.get("following_id")
    follower_id1 = ObjectId(follower_id)
    following_id1 = ObjectId(following_id)
    followee = follower_table.find_one({'follower_id':follower_id1, 'following_id':following_id1})
    # followee = collection.find_one({'_id':following_id})
    output={}
    # if followee['private'] == "yes":
    if followee is None:
        x = datetime.now()
        # x1 = json.dumps(x, default=json_util.default)
        # print(x1)
        queryObject = {
            'follower_id': follower_id1,
            'following_id': following_id1,
            'followed_time': str(x)
        }
        query = follower_table.insert_one(queryObject) #Requested table
        output['response'] = "followed"
        return JSONEncoder().encode(output)
    else:
        # print()
        # queryObject = {
        #     'follower_id': follower_id,
        #     'following_id': following_id,
        #     'followed_time':datetime.now()
        # }
        # query = follower_table.insert_one(queryObject) #following table
        output['response'] = "user exist"
        return JSONEncoder().encode(output)






@app.route('/unfollow', methods=['POST'])
def unfollowie():
    follower_id = request.values.get("follower_id") 
    following_id = request.values.get("following_id")
    follower_id1 = ObjectId(follower_id)
    following_id1 = ObjectId(following_id)
    followee = follower_table.find_one({'follower_id':follower_id1, 'following_id':following_id1})
    # followee = collection.find_one({'_id':following_id})
    output={}
    # if followee['private'] == "yes":
    if followee is None:
        
        output['response'] = "user does not exist"
        return JSONEncoder().encode(output)
    else:
        # print()
        # queryObject = {
        #     'follower_id': follower_id,
        #     'following_id': following_id,
        #     'followed_time':datetime.now()
        # }
        # query = follower_table.insert_one(queryObject) #following table
        print()
        queryObject = {
            'follower_id': follower_id1,
            'following_id': following_id1
        }
        query = follower_table.delete_one(queryObject) #Requested table
        output['response'] = "unfollowed"
        return JSONEncoder().encode(output)






@app.route('/followie', methods=['POST'])
def followie():
    follower_id = request.values.get("follower_id") 
    following_id = request.values.get("following_id")
    print(follower_id)
    print(following_id)
    follower_id1 = ObjectId(follower_id)
    print(follower_id1)
    following_id1 = ObjectId(following_id)
    print(following_id1)
    followee = follower_table.find_one({'follower_id':follower_id1, 'following_id':following_id1}) #follower_id mean user is folloeing with follower_id to following_id
    output={}
    if followee is None:
        print("Follow")
        # queryObject = {
        #     'follower_id': follower_id,
        #     'following_id': following_id,
        #     'followed_time':datetime.now()
        # }
        # query = follower_request.insert_one(queryObject) #Requested table
        output['response'] = "Follow"
        return JSONEncoder().encode(output)
    else:
        print("Friend")
        # queryObject = {
        #     'follower_id': follower_id,
        #     'following_id': following_id,
        #     'followed_time':datetime.now()
        # }
        # query = follower_table.insert_one(queryObject) #following table
        output['response'] = "Friend"
        return JSONEncoder().encode(output)




@app.route('/follow_request_accept', methods=['POST'])
def follow_request_accept():
    follower_id = request.values.get("follower_id") 
    following_id = request.values.get("following_id")
    # followee = collection.find_one({'_id':following_id})
    # if followee['private'] == "yes":
    #     print()
    #     queryObject = {
    #         'follower_id': follower_id,
    #         'following_id': following_id,
    #         'followed_time':datetime.now()
    #     }
    #     query = collection.insert_one(queryObject) #Requested table
    # else:
    #     print()
    output = {}
    queryObject = {
        'follower_id': follower_id,
        'following_id': following_id,
        'followed_time':datetime.now()
    }
    query = follower_table.insert_one(queryObject) #adding to following table
    output['response'] = "request_accepted"
    return JSONEncoder().encode(output)








@app.route('/follow_request_decline', methods=['POST'])
def follow_request_decline():
    follower_id = request.values.get("follower_id") 
    following_id = request.values.get("following_id")
    # followee = collection.find_one({'_id':following_id})
    # if followee['private'] == "yes":
    #     print()
    #     queryObject = {
    #         'follower_id': follower_id,
    #         'following_id': following_id,
    #         'followed_time':datetime.now()
    #     }
    #     query = collection.insert_one(queryObject) #Requested table
    # else:
    #     print()
    output={}
    queryObject = {
        'follower_id': follower_id,
        'following_id': following_id,
        'followed_time':datetime.now()
    }
    query = follower_request.delete_one(queryObject) #delete from following table
    output['response'] = "request_decline"
    return JSONEncoder().encode(output)



@app.route('/unfollow', methods=['POST'])
def unfollow():
    follower_id = request.values.get("follower_id") 
    following_id = request.values.get("following_id")
    output={}
    queryObject = {
        'follower_id': follower_id,
        'following_id': following_id,
        'followed_time':datetime.now()
    }
    query = collection.delete_one(queryObject)
    output['response'] = "unfollowed"
    return JSONEncoder().encode(output)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



@app.route('/insert-one/<name>/<id>/', methods=['GET'])
def insertOne(name, id):
    queryObject = {
        'username': name,
        'name': id,
    }
    query = collection.insert_one(queryObject)
    return "Query inserted...!!!"


# ####### getting errror in this api ##############
# @app.route('/find-one/<argument>/<value>/', methods=['GET'])
# def findOne(argument, value):
#     queryObject = {argument: value}
#     query = collection.find_one(queryObject)
#     query.pop('_id')
#     return jsonify(query)



@app.route('/find-one/<argument>/<value>/', methods=['GET'])
def findOne(argument, value):
    queryObject = {argument: value}
    query = collection.find_one(queryObject)
    query.pop('_id')
    return jsonify(query)


@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['GET'])
def update(key, value, element, updateValue):
    queryObject = {key: value}
    updateObject = {element: updateValue}#{"age": 23}
    query = collection.update_one(queryObject, {'$set': updateObject})
    if query.acknowledged:
        return "Update Successful"
    else:
        return "Update Unsuccessful"




@app.route('/star', methods=['GET','POST'])
def add_star():
#   star = mongo.db.stars
#   requestData =request.get_json()
#   data = json.loads(request.data)
#   name = data['name']
  name=request.values.get("name") 
#   distance = request.json['distance']
  star_id = collection.insert({'name': name})
  new_star = collection.find_one({'_id': star_id })
  output = {'name' : new_star['name']}
  return jsonify({'result' : output})



##################### getting error in this api #####################
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})

    return jsonify({'you sent this': json['text']})




#########################################################Search api ###################################################

##getting error ####
@app.route('/search', methods=['POST'])
def search():
    search = request.values.get("search") 
    print(len(search))
    if len(search) == 0:
        output = {}
        print('*')
    else:
        v1 = '.*'+search+'.*'
        rgx = re.compile(v1, re.IGNORECASE)
        print(rgx)


        queryObject = {"username": rgx}
        query = collection.find(queryObject) #profile table
        output = {}
        abc = []
        i = 0
        print(query)
        for x in query:
            abc.append(x)
            print(x)
        print(abc)



        queryObject1 = {"hashtag": rgx}
        query1 = collection.find(queryObject1) #hashtag table
        # output = {}
        abc1 = []
        i = 0
        print(query1)
        for y in query1:
            abc1.append(y)
            print(y)
        print(abc1)



        queryObject2 = {"sound": rgx}
        query2 = collection.find(queryObject2) #sound table
        # output = {}
        abc2 = []
        i = 0
        print(query2)
        for z in query2:
            abc2.append(z)
            print(z)
        print(abc2)


        queryObject3 = {"video": rgx}
        query3 = collection.find(queryObject3) #video table
        # output = {}
        abc3 = []
        i = 0
        print(query3)
        for a in query3:
            abc3.append(a)
            print(a)
        print(abc3)



        output["users"] = abc
        output["hashtags"] = abc1
        output["sounds"] = abc2
        output["videos"] = abc3
    return JSONEncoder().encode(output)


### getting error ###

@app.route('/searchUser', methods=['POST'])
def searchUser():
    search = request.values.get("search") 
    # if len(search) == 0:
    #     output = {}
    #     print('*')
    # else:
    v1 = '.*'+search+'.*'
    rgx = re.compile(v1, re.IGNORECASE)
    print(rgx)


    queryObject = {"username": rgx}
    query = collection.find(queryObject) #profile table
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["users"] = abc
    return JSONEncoder().encode(output)








#######################################################bookmark/videoapi#############################################


@app.route('/bookmark/videos', methods=['POST'])
def bookmarkVideos():
    user_id = request.values.get("user_id")
    print(user_id)
    user_id1 = ObjectId(user_id)
    query = bookmarks.aggregate([
            {"$match": {"user_id": user_id1, "type":'videos'}},
            {"$sort": {"bookmark_time": 1}},
            { "$lookup": {
                'from': 'videos',
                'localField': 'element_id',
                'foreignField': "_id",
                'as': "videoinfo"
            } },
            { "$unwind": "$videoinfo" },
            { "$project": {
                "bookmark_time":1,
                "videoinfo._id": 1,
                "videoinfo.username": 1,
                "videoinfo.img_url":1
            } }
        ])
    abc = []
    output = {}
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output['hashtags'] = abc
    return JSONEncoder().encode(output)



@app.route('/bookmark/AddVideos', methods=['POST'])
def bookmarkAddVideos():
    user_id = request.values.get("user_id") 
    video_id = request.values.get("video_id") 
    # query = collection.find()
    types = 'video'
    bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':video_id })
    if bkmk is None:
        queryObject = {
                'user_id': user_id,
                'element_id': video_id,
                'bookmark_time':datetime.now(),
                'types': types
            }
        query = bookmarks.insert_one(queryObject) #bookmark table
    else:
        queryObject = {'user_id':user_id, 'video_id':video_id }
        updateObject = {'bookmark_time':datetime.now()}
        query = bookmarks.update_one(queryObject, {'$set': updateObject})
        print('update')
    return "Query Inserted!!"



@app.route('/bookmark/RemoveVideos', methods=['POST'])
def bookmarkRemoveVideos():
    id = request.values.get("_id")
    query = bookmarks.delete_one({'_id':id}) #bookmark table
    return "Query Deleted!!"

###################################################bookmark/hastag############################################

@app.route('/bookmark/hashtags', methods=['POST'])
def bookmarkHastags():
    user_id = request.values.get("user_id")
    print(user_id)
    user_id1 = ObjectId(user_id)

    query = bookmarks.aggregate([
        {"$match": {"user_id": user_id1, "type":'hashtag'}},
        {"$sort": {"bookmark_time": 1}},
        { "$lookup": {
            'from': 'hashtags',
            'localField': 'element_id',
            'foreignField': "_id",
            'as': "hashtaginfo"
        } },
        { "$unwind": "$hashtaginfo" },
        { "$project": {
            "bookmark_time":1,
            "hashtaginfo._id": 1,
            "hashtaginfo.name": 1
        } }
    ])
    abc = []
    output = {}
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output['hashtags'] = abc
    return JSONEncoder().encode(output)


############################################################# addhastag ###############################


@app.route('/bookmark/AddHashtags', methods=['POST'])
def bookmarkAddHashtags():
    user_id = request.values.get("user_id") 
    hashtag_id = request.values.get("hashtag_id") 
    # query = collection.find()
    types = 'hashtag'
    bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':hashtag_id })
    if bkmk is None:
        queryObject = {
                'user_id': user_id,
                'element_id': hashtag_id,
                'bookmark_time':datetime.now(),
                'types': types
            }
        query = bookmarks.insert_one(queryObject) #bookmark table
    else:
        queryObject = {'user_id':user_id, 'element_id':hashtag_id }
        updateObject = {'bookmark_time':datetime.now()}
        query = bookmarks.update_one(queryObject, {'$set': updateObject})
        print('update')
    return "Query Inserted!!"


@app.route('/bookmark/RemoveHashtags', methods=['POST'])
def bookmarkRemoveHashtags():
    id = request.values.get("_id")
    query = bookmarks.delete_one({'_id':id}) #bookmark table
    return "Query Deleted!!"




@app.route('/bookmark/sounds', methods=['POST'])
def bookmarkSounds():
    user_id = request.values.get("user_id")
    print(user_id)
    user_id1 = ObjectId(user_id)

    query = bookmarks.aggregate([
        {"$match": {"user_id": user_id1, "type":'sounds'}},
        {"$sort": {"bookmark_time": 1}},
        { "$lookup": {
            'from': 'sounds',
            'localField': 'element_id',
            'foreignField': "_id",
            'as': "soundinfo"
        } },
        { "$unwind": "$soundinfo" },
        { "$project": {
            "bookmark_time":1,
            "soundinfo._id": 1,
            "soundinfo.name": 1
        } }
    ])
    abc = []
    output = {}
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output['hashtags'] = abc
    return JSONEncoder().encode(output)


@app.route('/bookmark/AddSound', methods=['POST'])
def bookmarkAddSound():
    user_id = request.values.get("user_id") 
    sound_id = request.values.get("sound_id") 
    # query = collection.find()
    types = 'sound'
    bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':sound_id })
    if bkmk is None:
        queryObject = {
                'user_id': user_id,
                'element_id': sound_id,
                'bookmark_time':datetime.now(),
                'types': types
            }
        query = bookmarks.insert_one(queryObject) #bookmark table
    else:
        queryObject = {'user_id':user_id, 'element_id':sound_id }
        updateObject = {'bookmark_time':datetime.now()}
        query = bookmarks.update_one(queryObject, {'$set': updateObject})
        print('update')
    return "Query Inserted!!"



@app.route('/bookmark/RemoveSound', methods=['POST'])
def bookmarkRemoveSound():
    id = request.values.get("_id")
    query = bookmarks.delete_one({'_id':id}) #bookmark table
    return "Query Deleted!!"



@app.route('/bookmark/effects', methods=['POST'])
def bookmarkEffects():
    user_id = request.values.get("user_id")
    print(user_id)
    user_id1 = ObjectId(user_id)

    query = bookmarks.aggregate([
        {"$match": {"user_id": user_id1, "type":'effects'}},
        {"$sort": {"bookmark_time": 1}},
        { "$lookup": {
            'from': 'effects',
            'localField': 'element_id',
            'foreignField': "_id",
            'as': "effectinfo"
        } },
        { "$unwind": "$effectinfo" },
        { "$project": {
            "bookmark_time":1,
            "effectinfo._id": 1,
            "effectinfo.name": 1
        } }
    ])
    abc = []
    output = {}
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output['hashtags'] = abc
    return JSONEncoder().encode(output)





@app.route('/bookmark/AddEffect', methods=['POST'])
def bookmarkAddEffect():
    user_id = request.values.get("user_id") 
    effect_id = request.values.get("effect_id") 
    # query = collection.find()
    types = 'effect'
    bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':effect_id })
    if bkmk is None:
        queryObject = {
                'user_id': user_id,
                'element_id': effect_id,
                'bookmark_time':datetime.now(),
                'types': types
            }
        query = bookmarks.insert_one(queryObject) #bookmark table
    else:
        queryObject = {'user_id':user_id, 'element_id':effect_id }
        updateObject = {'bookmark_time':datetime.now()}
        query = bookmarks.update_one(queryObject, {'$set': updateObject})
        print('update')
    return "Query Inserted!!"


@app.route('/bookmark/RemoveEffect', methods=['POST'])
def bookmarkRemoveEffect():
    id = request.values.get("_id")
    query = bookmarks.delete_one({'_id':id}) #bookmark table
    return "Query Deleted!!"


############################################# REGISTRATION API ###############################################

#################### wk #########################
@app.route('/searchtabs', methods=['POST'])
def findAllss():
    values = request.values.get("search") 
    print(len(values))
    if len(values) == 0:
        output = {}
        print('*')
    else:
        v1 = '.*'+values+'.*'
        rgx = re.compile(v1, re.IGNORECASE)
        print(rgx)
        queryObject = {"username": rgx}
        query = collection.find(queryObject)
        output = {}
        abc = []
        i = 0
        print(query)
        for x in query:
            abc.append(x)
            print(x)
        print(abc)
        output["users"] = abc
    return JSONEncoder().encode(output)


##################### getting error in this api #####################
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})

    return jsonify({'you sent this': json['text']})


  
  
  
  
  
  

#########################################################Search api ###################################################

## wk ####
@app.route('/search', methods=['POST'])
def search():
    search = request.values.get("search") 
    print(len(search))
    if len(search) == 0:
        output = {}
        print('*')
    else:
        v1 = '.*'+search+'.*'
        rgx = re.compile(v1, re.IGNORECASE)
        print(rgx)


        queryObject = {"username": rgx}
        query = collection.find(queryObject) #profile table
        output = {}
        abc = []
        i = 0
        print(query)
        for x in query:
            abc.append(x)
            print(x)
        print(abc)



        queryObject1 = {"hashtag": rgx}
        query1 = collection.find(queryObject1) #hashtag table
        # output = {}
        abc1 = []
        i = 0
        print(query1)
        for y in query1:
            abc1.append(y)
            print(y)
        print(abc1)



        queryObject2 = {"sound": rgx}
        query2 = collection.find(queryObject2) #sound table
        # output = {}
        abc2 = []
        i = 0
        print(query2)
        for z in query2:
            abc2.append(z)
            print(z)
        print(abc2)


        queryObject3 = {"video": rgx}
        query3 = collection.find(queryObject3) #video table
        # output = {}
        abc3 = []
        i = 0
        print(query3)
        for a in query3:
            abc3.append(a)
            print(a)
        print(abc3)



        output["users"] = abc
        output["hashtags"] = abc1
        output["sounds"] = abc2
        output["videos"] = abc3
    return JSONEncoder().encode(output)



@app.route('/searchUser', methods=['POST'])
def searchUser():
    search = request.values.get("search") 
    # if len(search) == 0:
    #     output = {}
    #     print('*')
    # else:
    v1 = '.*'+search+'.*'
    rgx = re.compile(v1, re.IGNORECASE)
    print(rgx)


    queryObject = {"username": rgx}
    query = collection.find(queryObject) #profile table
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["users"] = abc
    return JSONEncoder().encode(output)

  
  #################################### REGISTRATION API #################################################################
  
  
  
  
  
############################################# REGISTRATION API ###############################################


@app.route('/registration/email12', methods=['POST'])
def email12():
    e_mail = request.values.get("emailid")
    print(e_mail)
    # query = collection.find()
    # types = 'effect'
    a = ""
    output = {}
    bkmk = registartion.find_one({'email':e_mail})
    print(bkmk)
    if bkmk is None:
        # queryObject = {
        #         'email':e_mail
        #     }
        # emailOtp(e_mail)
        output["response"] = "success"
        return JSONEncoder().encode(output)
        # a = "success"
        # return "success" 
        # query = registartion.insert_one(queryObject) #registartion table
    else:
        # queryObject = {'user_id':user_id, 'element_id':effect_id }
        # updateObject = {'bookmark_time':datetime.now()}
        # query = bookmarks.update_one(queryObject, {'$set': updateObject})
        # print('update')
        output["response"] = "registerd"
        return JSONEncoder().encode(output)

  
#### getting error here ########
@app.route('/registration/sendemailOtp', methods=['POST'])
def emailOtp():
    e_mail = request.values.get("emailid")
    print(e_mail)
    emailOtps = int(random.randint(1000,9999))
    print(random.randint(1000,9999))
    bkmk = otp.find_one({'email':e_mail})
    print(bkmk)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    output={}
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login("testmailfear@gmail.com", "@kshay12")
    
    # message to be sent
    message = """Subject: SMTP e-mail test

                This is a test e-mail message.
                """ + "Otp for verification " + str(emailOtps) 
    
    # sending the mail
    s.sendmail("testmailfear@gmail.com", e_mail, message)
    
    # terminating the session
    s.quit()
    if bkmk is None:
        queryObject = {
                'email':e_mail,
                'otp_email':emailOtps
            }
        query = otp.insert_one(queryObject) #Otp table
        output["response"] = "success"
        return JSONEncoder().encode(output)
    else:
        queryObject = {'email':e_mail}
        # updateObject = {'bookmark_time':datetime.now()}
        updateObject ={'otp_email': emailOtps}
        query = otp.update_one(queryObject, {'$set': updateObject})
        output["response"] = "success"
        return JSONEncoder().encode(output)
        # output["response"] = "success"
        # return JSONEncoder().encode(output)
        
        
        
        
@app.route('/registration/phone', methods=['POST'])
def phone():
    p_hone = request.values.get("p_hone")
    # query = collection.find()
    # types = 'effect'
    bkmk = registartion.find_one({'phone':p_hone})
    if bkmk is None:
        # queryObject = {
        #         'email':e_mail
        #     }
        phoneOtp(p_hone)
        return "otp send"
        # query = registartion.insert_one(queryObject) #registartion table
    else:
        # queryObject = {'user_id':user_id, 'element_id':effect_id }
        # updateObject = {'bookmark_time':datetime.now()}
        # query = bookmarks.update_one(queryObject, {'$set': updateObject})
        # print('update')
        return "User Registred!"


# @app.route('/registration/emailOtp', methods=['POST'])
def phoneOtp(p_hone):
    print(p_hone)
    phoneOtps = int(random.randint(1000,9999))
    print(random.randint(1000,9999))
    bkmk = otp.find_one({'phone':p_hone})
    print(bkmk)
    account_sid = 'ACe975581ef18a344680b31468b79d4cd1'
    auth_token = 'dc8eb786d2a005db9d3a7a45095e34fa'
    
    client = Client(account_sid, auth_token)
    
    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_='+12034036973',
                                body ='Your SwipeUp Otp Verification is: ' + str(phoneOtps),
                                to = '+91'+str(p_hone)
                            )
    
    print(message.sid)
    if bkmk is None:
        queryObject = {
                'phone':p_hone,
                'otp_phone':phoneOtps
            }
        query = otp.insert_one(queryObject) #Otp table
        return "Query Inserted1 !!"
    else:
        queryObject = {'phone':p_hone}
        # updateObject = {'bookmark_time':datetime.now()}
        updateObject ={'otp_phone': phoneOtps}
        query = otp.update_one(queryObject, {'$set': updateObject})
        return "Query Inserted!!"

############# wk ###########################
@app.route('/otpVerfication', methods=['POST'])
def OtpVerify():
    user_id = request.values.get("user_id")
    o_t_p = request.values.get("otp")
    # query = collection.find()
    # types = 'effect'
    output={}
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, user_id)):
        print("Valid Email")
        bkmk = otp.find_one({'email': user_id, 'otp_email':int(o_t_p)})
        if bkmk is None:
            output["response"] = "wrong otp"
            return JSONEncoder().encode(output)
            # return "otp wrong!"
        else:
            bkmk1 = registartion.insert_one({"email": user_id})
            output["response"] = "verified"
            return JSONEncoder().encode(output)
            return "otp verified!"
    else:
        print("Invalid Email")
        bkmk = otp.find_one({'phone': user_id, 'otp_phone':int(o_t_p)})
        if bkmk is None:
            output["response"] = "wrong otp"
            return JSONEncoder().encode(output)
        else:
            bkmk1 = registartion.insert_one({"phone": user_id})
            output["response"] = "verified"
            return JSONEncoder().encode(output)

@app.route('/registration/email12', methods=['POST'])
def email12():
    e_mail = request.values.get("emailid")
    print(e_mail)
    # query = collection.find()
    # types = 'effect'
    a = ""
    output = {}
    bkmk = registartion.find_one({'email':e_mail})
    print(bkmk)
    if bkmk is None:
        # queryObject = {
        #         'email':e_mail
        #     }
        # emailOtp(e_mail)
        output["response"] = "success"
        return JSONEncoder().encode(output)
        # a = "success"
        # return "success" 
        # query = registartion.insert_one(queryObject) #registartion table
    else:
        # queryObject = {'user_id':user_id, 'element_id':effect_id }
        # updateObject = {'bookmark_time':datetime.now()}
        # query = bookmarks.update_one(queryObject, {'$set': updateObject})
        # print('update')
        output["response"] = "registerd"
        return JSONEncoder().encode(output)

#### getting error here ########
@app.route('/registration/sendemailOtp', methods=['POST'])
def emailOtp():
    e_mail = request.values.get("emailid")
    print(e_mail)
    emailOtps = int(random.randint(1000,9999))
    print(random.randint(1000,9999))
    bkmk = otp.find_one({'email':e_mail})
    print(bkmk)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    output={}
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login("testmailfear@gmail.com", "@kshay12")
    
    # message to be sent
    message = """Subject: SMTP e-mail test

                This is a test e-mail message.
                """ + "Otp for verification " + str(emailOtps) 
    
    # sending the mail
    s.sendmail("testmailfear@gmail.com", e_mail, message)
    
    # terminating the session
    s.quit()
    if bkmk is None:
        queryObject = {
                'email':e_mail,
                'otp_email':emailOtps
            }
        query = otp.insert_one(queryObject) #Otp table
        output["response"] = "success"
        return JSONEncoder().encode(output)
    else:
        queryObject = {'email':e_mail}
        # updateObject = {'bookmark_time':datetime.now()}
        updateObject ={'otp_email': emailOtps}
        query = otp.update_one(queryObject, {'$set': updateObject})
        output["response"] = "success"
        return JSONEncoder().encode(output)
        # output["response"] = "success"
        # return JSONEncoder().encode(output)


@app.route('/registration/phone', methods=['POST'])
def phone():
    p_hone = request.values.get("p_hone")
    # query = collection.find()
    # types = 'effect'
    bkmk = registartion.find_one({'phone':p_hone})
    if bkmk is None:
        # queryObject = {
        #         'email':e_mail
        #     }
        phoneOtp(p_hone)
        return "otp send"
        # query = registartion.insert_one(queryObject) #registartion table
    else:
        # queryObject = {'user_id':user_id, 'element_id':effect_id }
        # updateObject = {'bookmark_time':datetime.now()}
        # query = bookmarks.update_one(queryObject, {'$set': updateObject})
        # print('update')
        return "User Registred!"


# @app.route('/registration/emailOtp', methods=['POST'])
def phoneOtp(p_hone):
    print(p_hone)
    phoneOtps = int(random.randint(1000,9999))
    print(random.randint(1000,9999))
    bkmk = otp.find_one({'phone':p_hone})
    print(bkmk)
    account_sid = 'ACe975581ef18a344680b31468b79d4cd1'
    auth_token = 'dc8eb786d2a005db9d3a7a45095e34fa'
    
    client = Client(account_sid, auth_token)
    
    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_='+12034036973',
                                body ='Your SwipeUp Otp Verification is: ' + str(phoneOtps),
                                to = '+91'+str(p_hone)
                            )
    
    print(message.sid)
    if bkmk is None:
        queryObject = {
                'phone':p_hone,
                'otp_phone':phoneOtps
            }
        query = otp.insert_one(queryObject) #Otp table
        return "Query Inserted1 !!"
    else:
        queryObject = {'phone':p_hone}
        # updateObject = {'bookmark_time':datetime.now()}
        updateObject ={'otp_phone': phoneOtps}
        query = otp.update_one(queryObject, {'$set': updateObject})
        return "Query Inserted!!"

############# error ###########################
@app.route('/otpVerfication', methods=['POST'])
def OtpVerify():
    user_id = request.values.get("user_id")
    o_t_p = request.values.get("otp")
    # query = collection.find()
    # types = 'effect'
    output={}
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, user_id)):
        print("Valid Email")
        bkmk = otp.find_one({'email': user_id, 'otp_email':int(o_t_p)})
        if bkmk is None:
            output["response"] = "wrong otp"
            return JSONEncoder().encode(output)
            # return "otp wrong!"
        else:
            bkmk1 = registartion.insert_one({"email": user_id})
            output["response"] = "verified"
            return JSONEncoder().encode(output)
            return "otp verified!"
    else:
        print("Invalid Email")
        bkmk = otp.find_one({'phone': user_id, 'otp_phone':int(o_t_p)})
        if bkmk is None:
            output["response"] = "wrong otp"
            return JSONEncoder().encode(output)
        else:
            bkmk1 = registartion.insert_one({"phone": user_id})
            output["response"] = "verified"
            return JSONEncoder().encode(output)



    # if e_mail is None:
    #     bkmk = otp.find_one({'phone':p_hone, 'otp_phone':otp_phone})
    # elif p_hone is None:
    #     bkmk = otp.find_one({'email':e_mail, 'otp_email':otp_email})
    # if bkmk is None:
    #     # queryObject = {
    #     #         'email':e_mail
    #     #     }
    #     # phoneOtp(p_hone)
    #     return "please check Otp"
    #     # query = registartion.insert_one(queryObject) #registartion table
    # else:
    #     # queryObject = {'user_id':user_id, 'element_id':effect_id }
    #     # updateObject = {'bookmark_time':datetime.now()}
    #     # query = bookmarks.update_one(queryObject, {'$set': updateObject})
    #     # print('update')
    #     return "Otp Verified"


@app.route('/registration/username', methods=['POST'])
def username():
    u_sername = request.values.get("username")
    user_id = request.values.get("user_id")
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    # if(re.search(regex, e_mail)):
    #     print("Valid Email")
    #     bkmk = registartion.find_one({'username':u_sername, 'email':e_mail})
    # else:
    #     print("Invalid Email")
    #     bkmk = registartion.find_one({'username':u_sername, 'phone':e_mail})

    # query = collection.find()
    # types = 'effect'
    output = {}
    bkmk = registartion.find_one({'username':u_sername})
    if bkmk is None:
        if(re.search(regex, user_id)):
            queryObject = {'email':user_id}
            updateObject = {'username':u_sername}
            query = registartion.update_one(queryObject, {'$set': updateObject})
            print('update email')
            output["response"] = "verified"
            return JSONEncoder().encode(output)
        else:
            queryObject = {'phone':user_id}
            updateObject = {'username':u_sername}
            query = registartion.update_one(queryObject, {'$set': updateObject})
            output["response"] = "verified"
            return JSONEncoder().encode(output)
    else:
        # queryObject = {'user_id':user_id, 'element_id':effect_id }
        # updateObject = {'bookmark_time':datetime.now()}
        # query = bookmarks.update_one(queryObject, {'$set': updateObject})
        # print('update')
        output["response"] = "username taken"
        return JSONEncoder().encode(output)


@app.route('/registration/pagename', methods=['POST'])
def pagename():
    p_agename = request.values.get("pagename")
    user_id = request.values.get("user_id")
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    # if(re.search(regex, e_mail)):
    #     print("Valid Email")
    #     bkmk = registartion.find_one({'username':u_sername, 'email':e_mail})
    # else:
    #     print("Invalid Email")
    #     bkmk = registartion.find_one({'username':u_sername, 'phone':e_mail})

    # query = collection.find()
    # types = 'effect'
    output = {}
    bkmk = registartion.find_one({'pagename':p_agename})
    if bkmk is None:
        if(re.search(regex, user_id)):
            queryObject = {'email':user_id}
            updateObject = {'pagename':p_agename}
            query = registartion.update_one(queryObject, {'$set': updateObject})
            output["response"] = "verified"
            return JSONEncoder().encode(output)
        else:
            queryObject = {'phone':user_id}
            updateObject = {'pagename':p_agename}
            query = registartion.update_one(queryObject, {'$set': updateObject})
            output["response"] = "verified"
            return JSONEncoder().encode(output)
    else:
        # queryObject = {'user_id':user_id, 'element_id':effect_id }
        # updateObject = {'bookmark_time':datetime.now()}
        # query = bookmarks.update_one(queryObject, {'$set': updateObject})
        # print('update')
        output["response"] = "taken"
        return JSONEncoder().encode(output)

######## error ##############################
@app.route('/registration/birthdate', methods=['POST'])
def birthdate():
    b_irthdate = request.values.get("birthdate")
    user_id = request.values.get("user_id")
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    # query = collection.find()
    # types = 'effect'
    # bkmk = registartion.find_one({'email':email})
    output = {}
    if(re.search(regex, user_id)):
        queryObject = {'email':user_id}
        updateObject = {'birthdate':b_irthdate}
        query = registartion.update_one(queryObject, {'$set': updateObject})
        output["response"] = "verified"
        return JSONEncoder().encode(output)
    else:
        queryObject = {'phone':user_id}
        updateObject = {'birthdate':b_irthdate}
        query = registartion.update_one(queryObject, {'$set': updateObject})
        output["response"] = "verified"
        return JSONEncoder().encode(output)
    # return "Query Inserted!!"


###### eroror ##############################
@app.route('/registration/password', methods=['POST'])
def password():
    p_assword = request.values.get("password")
    user_id = request.values.get("user_id")
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    a = p_assword.encode("utf-8")
    hashed = bcrypt.hashpw(a, bcrypt.gensalt(14))
    print(hashed)
    # query = collection.find()
    # types = 'effect'
    # bkmk = registartion.find_one({'email':email})
    output ={}
    if(re.search(regex, user_id)):
        queryObject = {'email': user_id}
        x123 = str(datetime.now())
        print(x123)
        updateObject = {'password':hashed, 'created_at':x123}
        query = registartion.update_one(queryObject, {'$set': updateObject})
        bkmk = registartion.find_one({'email':user_id})
        bkmk2 = collection.find_one({'email':user_id})
        if bkmk2 is None:
            bkmk1 = collection.insert_one({ 'register_id':bkmk['_id'],'email':bkmk['email'], 'birthdate':bkmk['birthdate'], 'username':bkmk['username'], 'pagename':bkmk['pagename']})
            print('update')
            output["response"] = "verified"
            return JSONEncoder().encode(output)
        else:
            output["response"] = "verified"
            return JSONEncoder().encode(output)
            # return "password Inserted!!"
    else:
        queryObject = {'phone':user_id}
        updateObject = {'password':hashed, 'created_at':datetime.now()}
        query = registartion.update_one(queryObject, {'$set': updateObject})
        bkmk = registartion.find_one({'phone':user_id})
        bkmk2 = collection.find_one({'phone':user_id})
        if bkmk2 is None:
            bkmk1 = collection.insert_one({ 'register_id':bkmk['_id'],'phone':bkmk['phone'], 'birthdate':bkmk['birthdate'], 'username':bkmk['username'], 'pagename':bkmk['pagename']})
            print('update')
            output["response"] = "verified"
            return JSONEncoder().encode(output)
        else:
            output["response"] = "verified"
            return JSONEncoder().encode(output)

###### erorr#################
@app.route('/signIIn', methods=['POST'])
def SignIn():
    user_id = request.values.get("user_id")
    print(user_id)
    paassword = request.values.get("password")
    a = paassword.encode("utf-8")
    print(a)
    print(paassword)
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    regex1 = "(0|91)?[7-9][0-9]{9}"
    # obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    # message = b"The answer is no"
    # print(message)
    # ciphertext = obj.encrypt(message)
    # print(ciphertext)


    # passworda = "super secret password"
    # print(passworda)
    # hashed = bcrypt.hashpw(a, bcrypt.gensalt(14))
    # print(hashed)
    # hashed1 = b'$2b$14$KmJZ7KQRfj/rka5C5JI6p.hh20FyWGHNdEqDgT6pBFiHE4t.U19Vm'
    # if bcrypt.checkpw(a, hashed1):
    #     print("It Matches!")
    # else:
    #     print("It Does not Match :(")
    # regex2  = "[7-9][0-9]{9}"
    # query = collection.find()
    # types = 'effect'
    # bkmk = registartion.find_one({'email':email})
    if(re.search(regex, user_id)):
        bkmk = registartion.find_one({'email':user_id})
        print(bkmk)
        output = {}
        abc = []
        print(bkmk['password'])
        if bcrypt.checkpw(a, bkmk['password']):
            print("It Matches!")
            bkmk = collection.find_one({'email':user_id})
            # for x in bkmk:
            #     print(x)
            print(bkmk)
            output["xyz"] = bkmk
            output["response"] = "verified"
            return JSONEncoder().encode(output)
        else:
            print("It Does not Match :(")
            output["response"] = "wrong password"
            return JSONEncoder().encode(output)
        # for x in bkmk:
        #     abc.append(x)
        #     print(x)
        # print(abc)
        # output["users"] = abc
        # queryObject = {'email':e_mail}
        # updateObject = {'password':p_assword}
        # query = registartion.update_one(queryObject, {'$set': updateObject})
        # return JSONEncoder().encode(output)
    elif(re.search(regex1, user_id)):
        bkmk = registartion.find_one({'phone':user_id})
        output = {}
        abc = []
        print(bkmk)
        # print(bkmk['password'])
        if bcrypt.checkpw(a, bkmk['password']):
            print("It Matches!")
            bkmk = collection.find_one({'phone':user_id})
            output["users"] = bkmk
            output["response"] = "verified"
            return JSONEncoder().encode(output)
        else:
            print("It Does not Match :(")
            output["response"] = "wrong password"
            return JSONEncoder().encode(output)
        # for x in bkmk:
        #     abc.append(x)
        # print(x)
        # print(abc)
        # output["users"] = abc
        # # queryObject = {'email':e_mail}
        # # updateObject = {'password':p_assword}
        # # query = registartion.update_one(queryObject, {'$set': updateObject})
        # return JSONEncoder().encode(output)
    else:
        bkmk = registartion.find_one({'username':user_id})
        output = {}
        abc = []
        print(bkmk)
        print(bkmk['password'])
        if bcrypt.checkpw(a, bkmk['password']):
            print("Its Matches!")
            bkmk = collection.find_one({'username':user_id})
            output["users"] = bkmk
            output["response"] = "verified"
            return JSONEncoder().encode(output)
        else:
            print("It Does not Match :(")
            output["response"] = "wrong password"
            return JSONEncoder().encode(output)
        # queryObject = {'email':e_mail}
        # updateObject = {'password':p_assword}
        # query = registartion.update_one(queryObject, {'$set': updateObject})
        # return JSONEncoder().encode(output)




#######################################
# @app.route('/findfriends', methods=['POST'])
# def findAlls():
#     values = request.values.get("username") 
#     print(len(values))
#     # if len(values) == 0:
#     #     output = {}
#     #     print('*')
#     # else:
#     v1 = '.*'+values+'.*'
#     rgx = re.compile(v1, re.IGNORECASE)
#     print(rgx)
#     queryObject = {"username": rgx}
#     query = collection.find(queryObject)
#     output = {}
#     abc = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x)
#         print(x)
#     print(abc)
#     output["users"] = abc
#     return JSONEncoder().encode(output)


# @app.route('/searchtabs', methods=['POST'])
# def findAllss():
#     values = request.values.get("search") 
#     print(len(values))
#     if len(values) == 0:
#         output = {}
#         print('*')
#     else:
#         v1 = '.*'+values+'.*'
#         rgx = re.compile(v1, re.IGNORECASE)
#         print(rgx)
#         queryObject = {"username": rgx}
#         query = collection.find(queryObject)
#         output = {}
#         abc = []
#         i = 0
#         print(query)
#         for x in query:
#             abc.append(x)
#             print(x)
#         print(abc)
#         output["users"] = abc
#     return JSONEncoder().encode(output)


# @app.route('/follow', methods=['POST'])
# def follow():
#     follower_id = request.values.get("follower_id") 
#     following_id = request.values.get("following_id")
#     followee = collection.find_one({'_id':following_id})
#     output={}
#     if followee['private'] == "yes":
#         print()
#         queryObject = {
#             'follower_id': follower_id,
#             'following_id': following_id,
#             'followed_time':datetime.now()
#         }
#         query = follower_request.insert_one(queryObject) #Requested table
#         output['response'] = "requested"
#         return JSONEncoder().encode(output)
#     else:
#         print()
#         queryObject = {
#             'follower_id': follower_id,
#             'following_id': following_id,
#             'followed_time':datetime.now()
#         }
#         query = follower_table.insert_one(queryObject) #following table
#         output['response'] = "followed"
#         return JSONEncoder().encode(output)



# @app.route('/follow', methods=['POST'])
# def follow():
#     follower_id = request.values.get("follower_id") 
#     following_id = request.values.get("following_id")
#     follower_id1 = ObjectId(follower_id)
#     following_id1 = ObjectId(following_id)
#     followee = follower_table.find_one({'follower_id':follower_id1, 'following_id':following_id1})
#     # followee = collection.find_one({'_id':following_id})
#     output={}
#     # if followee['private'] == "yes":
#     if followee is None:
#         x = datetime.now()
#         # x1 = json.dumps(x, default=json_util.default)
#         # print(x1)
#         queryObject = {
#             'follower_id': follower_id1,
#             'following_id': following_id1,
#             'followed_time': str(x)
#         }
#         query = follower_table.insert_one(queryObject) #Requested table
#         output['response'] = "followed"
#         return JSONEncoder().encode(output)
#     else:
#         # print()
#         # queryObject = {
#         #     'follower_id': follower_id,
#         #     'following_id': following_id,
#         #     'followed_time':datetime.now()
#         # }
#         # query = follower_table.insert_one(queryObject) #following table
#         output['response'] = "user exist"
#         return JSONEncoder().encode(output)



# @app.route('/unfollow', methods=['POST'])
# def unfollowie():
#     follower_id = request.values.get("follower_id") 
#     following_id = request.values.get("following_id")
#     follower_id1 = ObjectId(follower_id)
#     following_id1 = ObjectId(following_id)
#     followee = follower_table.find_one({'follower_id':follower_id1, 'following_id':following_id1})
#     # followee = collection.find_one({'_id':following_id})
#     output={}
#     # if followee['private'] == "yes":
#     if followee is None:
        
#         output['response'] = "user does not exist"
#         return JSONEncoder().encode(output)
#     else:
#         # print()
#         # queryObject = {
#         #     'follower_id': follower_id,
#         #     'following_id': following_id,
#         #     'followed_time':datetime.now()
#         # }
#         # query = follower_table.insert_one(queryObject) #following table
#         print()
#         queryObject = {
#             'follower_id': follower_id1,
#             'following_id': following_id1
#         }
#         query = follower_table.delete_one(queryObject) #Requested table
#         output['response'] = "unfollowed"
#         return JSONEncoder().encode(output)


# @app.route('/followie', methods=['POST'])
# def followie():
#     follower_id = request.values.get("follower_id") 
#     following_id = request.values.get("following_id")
#     print(follower_id)
#     print(following_id)
#     follower_id1 = ObjectId(follower_id)
#     print(follower_id1)
#     following_id1 = ObjectId(following_id)
#     print(following_id1)
#     followee = follower_table.find_one({'follower_id':follower_id1, 'following_id':following_id1}) #follower_id mean user is folloeing with follower_id to following_id
#     output={}
#     if followee is None:
#         print("Follow")
#         # queryObject = {
#         #     'follower_id': follower_id,
#         #     'following_id': following_id,
#         #     'followed_time':datetime.now()
#         # }
#         # query = follower_request.insert_one(queryObject) #Requested table
#         output['response'] = "Follow"
#         return JSONEncoder().encode(output)
#     else:
#         print("Friend")
#         # queryObject = {
#         #     'follower_id': follower_id,
#         #     'following_id': following_id,
#         #     'followed_time':datetime.now()
#         # }
#         # query = follower_table.insert_one(queryObject) #following table
#         output['response'] = "Friend"
#         return JSONEncoder().encode(output)









# @app.route('/follow_request_accept', methods=['POST'])
# def follow_request_accept():
#     follower_id = request.values.get("follower_id") 
#     following_id = request.values.get("following_id")
#     # followee = collection.find_one({'_id':following_id})
#     # if followee['private'] == "yes":
#     #     print()
#     #     queryObject = {
#     #         'follower_id': follower_id,
#     #         'following_id': following_id,
#     #         'followed_time':datetime.now()
#     #     }
#     #     query = collection.insert_one(queryObject) #Requested table
#     # else:
#     #     print()
#     output = {}
#     queryObject = {
#         'follower_id': follower_id,
#         'following_id': following_id,
#         'followed_time':datetime.now()
#     }
#     query = follower_table.insert_one(queryObject) #adding to following table
#     output['response'] = "request_accepted"
#     return JSONEncoder().encode(output)



# @app.route('/follow_request_decline', methods=['POST'])
# def follow_request_decline():
#     follower_id = request.values.get("follower_id") 
#     following_id = request.values.get("following_id")
#     # followee = collection.find_one({'_id':following_id})
#     # if followee['private'] == "yes":
#     #     print()
#     #     queryObject = {
#     #         'follower_id': follower_id,
#     #         'following_id': following_id,
#     #         'followed_time':datetime.now()
#     #     }
#     #     query = collection.insert_one(queryObject) #Requested table
#     # else:
#     #     print()
#     output={}
#     queryObject = {
#         'follower_id': follower_id,
#         'following_id': following_id,
#         'followed_time':datetime.now()
#     }
#     query = follower_request.delete_one(queryObject) #delete from following table
#     output['response'] = "request_decline"
#     return JSONEncoder().encode(output)



# @app.route('/unfollow', methods=['POST'])
# def unfollow():
#     follower_id = request.values.get("follower_id") 
#     following_id = request.values.get("following_id")
#     output={}
#     queryObject = {
#         'follower_id': follower_id,
#         'following_id': following_id,
#         'followed_time':datetime.now()
#     }
#     query = collection.delete_one(queryObject)
#     output['response'] = "unfollowed"
#     return JSONEncoder().encode(output)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# @app.route('/insert-one/<name>/<id>/', methods=['GET'])
# def insertOne(name, id):
#     queryObject = {
#         'username': name,
#         'name': id,
#     }
#     query = collection.insert_one(queryObject)
#     return "Query inserted...!!!"



# @app.route('/find-one/<argument>/<value>/', methods=['GET'])
# def findOne(argument, value):
#     queryObject = {argument: value}
#     query = collection.find_one(queryObject)
#     query.pop('_id')
#     return jsonify(query)

# @app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['GET'])
# def update(key, value, element, updateValue):
#     queryObject = {key: value}
#     updateObject = {element: updateValue}#{"age": 23}
#     query = collection.update_one(queryObject, {'$set': updateObject})
#     if query.acknowledged:
#         return "Update Successful"
#     else:
#         return "Update Unsuccessful"




# @app.route('/star', methods=['GET','POST'])
# def add_star():
# #   star = mongo.db.stars
# #   requestData =request.get_json()
# #   data = json.loads(request.data)
# #   name = data['name']
#   name=request.values.get("name") 
# #   distance = request.json['distance']
#   star_id = collection.insert({'name': name})
#   new_star = collection.find_one({'_id': star_id })
#   output = {'name' : new_star['name']}
#   return jsonify({'result' : output})


# @app.route('/api/post_some_data', methods=['POST'])
# def get_text_prediction():
#     """
#     predicts requested text whether it is ham or spam
#     :return: json
#     """
#     json = request.get_json()
#     print(json)
#     if len(json['text']) == 0:
#         return jsonify({'error': 'invalid input'})

#     return jsonify({'you sent this': json['text']})

# ##################################### SEARCH API ########################################

# @app.route('/search', methods=['POST'])
# def search():
#     search = request.values.get("search") 
#     print(len(search))
#     if len(search) == 0:
#         output = {}
#         print('*')
#     else:
#         v1 = '.*'+search+'.*'
#         rgx = re.compile(v1, re.IGNORECASE)
#         print(rgx)


#         queryObject = {"username": rgx}
#         query = collection.find(queryObject) #profile table
#         output = {}
#         abc = []
#         i = 0
#         print(query)
#         for x in query:
#             abc.append(x)
#             print(x)
#         print(abc)



#         queryObject1 = {"hashtag": rgx}
#         query1 = collection.find(queryObject1) #hashtag table
#         # output = {}
#         abc1 = []
#         i = 0
#         print(query1)
#         for y in query1:
#             abc1.append(y)
#             print(y)
#         print(abc1)



#         queryObject2 = {"sound": rgx}
#         query2 = collection.find(queryObject2) #sound table
#         # output = {}
#         abc2 = []
#         i = 0
#         print(query2)
#         for z in query2:
#             abc2.append(z)
#             print(z)
#         print(abc2)


#         queryObject3 = {"video": rgx}
#         query3 = collection.find(queryObject3) #video table
#         # output = {}
#         abc3 = []
#         i = 0
#         print(query3)
#         for a in query3:
#             abc3.append(a)
#             print(a)
#         print(abc3)



#         output["users"] = abc
#         output["hashtags"] = abc1
#         output["sounds"] = abc2
#         output["videos"] = abc3
#     return JSONEncoder().encode(output)


# @app.route('/searchUser', methods=['POST'])
# def searchUser():
#     search = request.values.get("search") 
#     # if len(search) == 0:
#     #     output = {}
#     #     print('*')
#     # else:
#     v1 = '.*'+search+'.*'
#     rgx = re.compile(v1, re.IGNORECASE)
#     print(rgx)


#     queryObject = {"username": rgx}
#     query = collection.find(queryObject) #profile table
#     output = {}
#     abc = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x)
#         print(x)
#     print(abc)
#     output["users"] = abc
#     return JSONEncoder().encode(output)


# ################################ BOOKMARKS API ########################################



# @app.route('/bookmark/videos', methods=['POST'])
# def bookmarkVideos():
#     user_id = request.values.get("user_id")
#     queryObject = {"user_id":user_id}
#     query = bookmarks.find(queryObject)
#     output = {}
#     abc = []
#     abc1 = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x['element_id'])
#     print(abc)
#     for y in abc:
#         video = collections.find_one({"_id": ObjectId(y)})
#         print(video)
#         abc1.append(video)
#         # output[i] = x
#         # output[i].pop('_id')
#         # i += 1
#         # print(x)
#     print(abc1)
#     output["users"] = abc1
#     # output["users"].pop('_id')

#     return JSONEncoder().encode(output)


# @app.route('/bookmark/AddVideos', methods=['POST'])
# def bookmarkAddVideos():
#     user_id = request.values.get("user_id") 
#     video_id = request.values.get("video_id") 
#     # query = collection.find()
#     types = 'video'
#     bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':video_id })
#     if bkmk is None:
#         queryObject = {
#                 'user_id': user_id,
#                 'element_id': video_id,
#                 'bookmark_time':datetime.now(),
#                 'types': types
#             }
#         query = bookmarks.insert_one(queryObject) #bookmark table
#     else:
#         queryObject = {'user_id':user_id, 'video_id':video_id }
#         updateObject = {'bookmark_time':datetime.now()}
#         query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         print('update')
#     return "Query Inserted!!"


# @app.route('/bookmark/RemoveVideos', methods=['POST'])
# def bookmarkRemoveVideos():
#     id = request.values.get("_id")
#     query = bookmarks.delete_one({'_id':id}) #bookmark table
#     return "Query Deleted!!"


# # @app.route('/bookmark/hashtags', methods=['POST'])
# # def bookmarkHastags():
# #     user_id = request.values.get("user_id")
# #     queryObject = {"user_id":user_id}
# #     query = bookmarks.find(queryObject)
# #     output = {}
# #     abc = []
# #     abc1 = []
# #     i = 0
# #     print(query)
# #     for x in query:
# #         abc.append(x['element_id'])
# #     print(abc)
# #     for y in abc:
# #         hashtag = collections.find_one({"_id": ObjectId(y)})
# #         print(hashtag)
# #         abc1.append(hashtag)
# #         # output[i] = x
# #         # output[i].pop('_id')
# #         # i += 1
# #         # print(x)
# #     print(abc1)
# #     output["users"] = abc1
# #     # output["users"].pop('_id')

# #     return JSONEncoder().encode(output)



# @app.route('/bookmark/hashtags', methods=['POST'])
# def bookmarkHastags():
#     user_id = request.values.get("user_id")
#     user_id1 = ObjectId(user_id)

#     query = bookmarks.aggregate([
#         {"$match": {"user_id": user_id1, "type":'hashtag'}},
#         {"$sort": {"bookmark_time": 1}},
#         { "$lookup": {
#             'from': 'hashtags',
#             'localField': 'element_id',
#             'foreignField': "_id",
#             'as': "hashtaginfo"
#         } },
#         { "$unwind": "$hashtaginfo" },
#         { "$project": {
#             "bookmark_time":1,
#             "hashtaginfo._id": 1,
#             "hashtaginfo.name": 1
#         } }
#     ])
#     abc = []
#     output = {}
#     for x in query:
#         abc.append(x)
#         print(x)
#     print(abc)
#     output['hashtags'] = abc
#     return JSONEncoder().encode(output)




# @app.route('/bookmark/AddHashtags', methods=['POST'])
# def bookmarkAddHashtags():
#     user_id = request.values.get("user_id") 
#     hashtag_id = request.values.get("hashtag_id") 
#     # query = collection.find()
#     types = 'hashtag'
#     bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':hashtag_id })
#     if bkmk is None:
#         queryObject = {
#                 'user_id': user_id,
#                 'element_id': hashtag_id,
#                 'bookmark_time':datetime.now(),
#                 'types': types
#             }
#         query = bookmarks.insert_one(queryObject) #bookmark table
#     else:
#         queryObject = {'user_id':user_id, 'element_id':hashtag_id }
#         updateObject = {'bookmark_time':datetime.now()}
#         query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         print('update')
#     return "Query Inserted!!"


# @app.route('/bookmark/RemoveHashtags', methods=['POST'])
# def bookmarkRemoveHashtags():
#     id = request.values.get("_id")
#     query = bookmarks.delete_one({'_id':id}) #bookmark table
#     return "Query Deleted!!"




# @app.route('/bookmark/sounds', methods=['POST'])
# def bookmarkSounds():
#     user_id = request.values.get("user_id")
#     queryObject = {"user_id":user_id}
#     query = bookmarks.find(queryObject)
#     output = {}
#     abc = []
#     abc1 = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x['element_id'])
#     print(abc)
#     for y in abc:
#         sound = collections.find_one({"_id": ObjectId(y)})
#         print(sound)
#         abc1.append(sound)
#         # output[i] = x
#         # output[i].pop('_id')
#         # i += 1
#         # print(x)
#     print(abc1)
#     output["users"] = abc1
#     # output["users"].pop('_id')

#     return JSONEncoder().encode(output)


# @app.route('/bookmark/AddSound', methods=['POST'])
# def bookmarkAddSound():
#     user_id = request.values.get("user_id") 
#     sound_id = request.values.get("sound_id") 
#     # query = collection.find()
#     types = 'sound'
#     bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':sound_id })
#     if bkmk is None:
#         queryObject = {
#                 'user_id': user_id,
#                 'element_id': sound_id,
#                 'bookmark_time':datetime.now(),
#                 'types': types
#             }
#         query = bookmarks.insert_one(queryObject) #bookmark table
#     else:
#         queryObject = {'user_id':user_id, 'element_id':sound_id }
#         updateObject = {'bookmark_time':datetime.now()}
#         query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         print('update')
#     return "Query Inserted!!"


# @app.route('/bookmark/RemoveSound', methods=['POST'])
# def bookmarkRemoveSound():
#     id = request.values.get("_id")
#     query = bookmarks.delete_one({'_id':id}) #bookmark table
#     return "Query Deleted!!"


# @app.route('/bookmark/effects', methods=['POST'])
# def bookmarkEffects():
#     user_id = request.values.get("user_id")
#     queryObject = {"user_id":user_id}
#     query = bookmarks.find(queryObject)
#     output = {}
#     abc = []
#     abc1 = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x['element_id'])
#     print(abc)
#     for y in abc:
#         effect = collections.find_one({"_id": ObjectId(y)})
#         print(effect)
#         abc1.append(effect)
#         # output[i] = x
#         # output[i].pop('_id')
#         # i += 1
#         # print(x)
#     print(abc1)
#     output["users"] = abc1
#     # output["users"].pop('_id')

#     return JSONEncoder().encode(output)


# @app.route('/bookmark/AddEffect', methods=['POST'])
# def bookmarkAddEffect():
#     user_id = request.values.get("user_id") 
#     effect_id = request.values.get("effect_id") 
#     # query = collection.find()
#     types = 'effect'
#     bkmk = bookmarks.find_one({'user_id':user_id, 'element_id':effect_id })
#     if bkmk is None:
#         queryObject = {
#                 'user_id': user_id,
#                 'element_id': effect_id,
#                 'bookmark_time':datetime.now(),
#                 'types': types
#             }
#         query = bookmarks.insert_one(queryObject) #bookmark table
#     else:
#         queryObject = {'user_id':user_id, 'element_id':effect_id }
#         updateObject = {'bookmark_time':datetime.now()}
#         query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         print('update')
#     return "Query Inserted!!"


# @app.route('/bookmark/RemoveEffect', methods=['POST'])
# def bookmarkRemoveEffect():
#     id = request.values.get("_id")
#     query = bookmarks.delete_one({'_id':id}) #bookmark table
#     return "Query Deleted!!"


# #################################### INBOX API ################################






# ###################################  Registration API ##########################


# @app.route('/registration/email12', methods=['POST'])
# def email12():
#     e_mail = request.values.get("emailid")
#     print(e_mail)
#     # query = collection.find()
#     # types = 'effect'
#     a = ""
#     output = {}
#     bkmk = registartion.find_one({'email':e_mail})
#     print(bkmk)
#     if bkmk is None:
#         # queryObject = {
#         #         'email':e_mail
#         #     }
#         # emailOtp(e_mail)
#         output["response"] = "success"
#         return JSONEncoder().encode(output)
#         # a = "success"
#         # return "success" 
#         # query = registartion.insert_one(queryObject) #registartion table
#     else:
#         # queryObject = {'user_id':user_id, 'element_id':effect_id }
#         # updateObject = {'bookmark_time':datetime.now()}
#         # query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         # print('update')
#         output["response"] = "registerd"
#         return JSONEncoder().encode(output)


# @app.route('/registration/sendemailOtp', methods=['POST'])
# def emailOtp():
#     e_mail = request.values.get("emailid")
#     print(e_mail)
#     emailOtps = int(random.randint(1000,9999))
#     print(random.randint(1000,9999))
#     bkmk = otp.find_one({'email':e_mail})
#     print(bkmk)
#     # creates SMTP session
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     output={}
#     # start TLS for security
#     s.starttls()
    
#     # Authentication
#     s.login("testmailfear@gmail.com", "@kshay12")
    
#     # message to be sent
#     message = """Subject: SMTP e-mail test

#                 This is a test e-mail message.
#                 """ + "Otp for verification " + str(emailOtps) 
    
#     # sending the mail
#     s.sendmail("testmailfear@gmail.com", e_mail, message)
    
#     # terminating the session
#     s.quit()
#     if bkmk is None:
#         queryObject = {
#                 'email':e_mail,
#                 'otp_email':emailOtps
#             }
#         query = otp.insert_one(queryObject) #Otp table
#         output["response"] = "success"
#         return JSONEncoder().encode(output)
#     else:
#         queryObject = {'email':e_mail}
#         # updateObject = {'bookmark_time':datetime.now()}
#         updateObject ={'otp_email': emailOtps}
#         query = otp.update_one(queryObject, {'$set': updateObject})
#         output["response"] = "success"
#         return JSONEncoder().encode(output)
#         # output["response"] = "success"
#         # return JSONEncoder().encode(output)


# @app.route('/registration/phone', methods=['POST'])
# def phone():
#     p_hone = request.values.get("p_hone")
#     # query = collection.find()
#     # types = 'effect'
#     bkmk = registartion.find_one({'phone':p_hone})
#     if bkmk is None:
#         # queryObject = {
#         #         'email':e_mail
#         #     }
#         phoneOtp(p_hone)
#         return "otp send"
#         # query = registartion.insert_one(queryObject) #registartion table
#     else:
#         # queryObject = {'user_id':user_id, 'element_id':effect_id }
#         # updateObject = {'bookmark_time':datetime.now()}
#         # query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         # print('update')
#         return "User Registred!"


# # @app.route('/registration/emailOtp', methods=['POST'])
# def phoneOtp(p_hone):
#     print(p_hone)
#     phoneOtps = int(random.randint(1000,9999))
#     print(random.randint(1000,9999))
#     bkmk = otp.find_one({'phone':p_hone})
#     print(bkmk)
#     account_sid = 'ACe975581ef18a344680b31468b79d4cd1'
#     auth_token = 'dc8eb786d2a005db9d3a7a45095e34fa'
    
#     client = Client(account_sid, auth_token)
    
#     ''' Change the value of 'from' with the number 
#     received from Twilio and the value of 'to'
#     with the number in which you want to send message.'''
#     message = client.messages.create(
#                                 from_='+12034036973',
#                                 body ='Your SwipeUp Otp Verification is: ' + str(phoneOtps),
#                                 to = '+91'+str(p_hone)
#                             )
    
#     print(message.sid)
#     if bkmk is None:
#         queryObject = {
#                 'phone':p_hone,
#                 'otp_phone':phoneOtps
#             }
#         query = otp.insert_one(queryObject) #Otp table
#         return "Query Inserted1 !!"
#     else:
#         queryObject = {'phone':p_hone}
#         # updateObject = {'bookmark_time':datetime.now()}
#         updateObject ={'otp_phone': phoneOtps}
#         query = otp.update_one(queryObject, {'$set': updateObject})
#         return "Query Inserted!!"


# @app.route('/otpVerfication', methods=['POST'])
# def OtpVerify():
#     user_id = request.values.get("user_id")
#     o_t_p = request.values.get("otp")
#     # query = collection.find()
#     # types = 'effect'
#     output={}
#     regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#     if(re.search(regex, user_id)):
#         print("Valid Email")
#         bkmk = otp.find_one({'email': user_id, 'otp_email':int(o_t_p)})
#         if bkmk is None:
#             output["response"] = "wrong otp"
#             return JSONEncoder().encode(output)
#             # return "otp wrong!"
#         else:
#             bkmk1 = registartion.insert_one({"email": user_id})
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#             return "otp verified!"
#     else:
#         print("Invalid Email")
#         bkmk = otp.find_one({'phone': user_id, 'otp_phone':int(o_t_p)})
#         if bkmk is None:
#             output["response"] = "wrong otp"
#             return JSONEncoder().encode(output)
#         else:
#             bkmk1 = registartion.insert_one({"phone": user_id})
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)



#     # if e_mail is None:
#     #     bkmk = otp.find_one({'phone':p_hone, 'otp_phone':otp_phone})
#     # elif p_hone is None:
#     #     bkmk = otp.find_one({'email':e_mail, 'otp_email':otp_email})
#     # if bkmk is None:
#     #     # queryObject = {
#     #     #         'email':e_mail
#     #     #     }
#     #     # phoneOtp(p_hone)
#     #     return "please check Otp"
#     #     # query = registartion.insert_one(queryObject) #registartion table
#     # else:
#     #     # queryObject = {'user_id':user_id, 'element_id':effect_id }
#     #     # updateObject = {'bookmark_time':datetime.now()}
#     #     # query = bookmarks.update_one(queryObject, {'$set': updateObject})
#     #     # print('update')
#     #     return "Otp Verified"


# @app.route('/registration/username', methods=['POST'])
# def username():
#     u_sername = request.values.get("username")
#     user_id = request.values.get("user_id")
#     regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#     # if(re.search(regex, e_mail)):
#     #     print("Valid Email")
#     #     bkmk = registartion.find_one({'username':u_sername, 'email':e_mail})
#     # else:
#     #     print("Invalid Email")
#     #     bkmk = registartion.find_one({'username':u_sername, 'phone':e_mail})

#     # query = collection.find()
#     # types = 'effect'
#     output = {}
#     bkmk = registartion.find_one({'username':u_sername})
#     if bkmk is None:
#         if(re.search(regex, user_id)):
#             queryObject = {'email':user_id}
#             updateObject = {'username':u_sername}
#             query = registartion.update_one(queryObject, {'$set': updateObject})
#             print('update email')
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#         else:
#             queryObject = {'phone':user_id}
#             updateObject = {'username':u_sername}
#             query = registartion.update_one(queryObject, {'$set': updateObject})
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#     else:
#         # queryObject = {'user_id':user_id, 'element_id':effect_id }
#         # updateObject = {'bookmark_time':datetime.now()}
#         # query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         # print('update')
#         output["response"] = "username taken"
#         return JSONEncoder().encode(output)


# @app.route('/registration/pagename', methods=['POST'])
# def pagename():
#     p_agename = request.values.get("pagename")
#     user_id = request.values.get("user_id")
#     regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#     # if(re.search(regex, e_mail)):
#     #     print("Valid Email")
#     #     bkmk = registartion.find_one({'username':u_sername, 'email':e_mail})
#     # else:
#     #     print("Invalid Email")
#     #     bkmk = registartion.find_one({'username':u_sername, 'phone':e_mail})

#     # query = collection.find()
#     # types = 'effect'
#     output = {}
#     bkmk = registartion.find_one({'pagename':p_agename})
#     if bkmk is None:
#         if(re.search(regex, user_id)):
#             queryObject = {'email':user_id}
#             updateObject = {'pagename':p_agename}
#             query = registartion.update_one(queryObject, {'$set': updateObject})
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#         else:
#             queryObject = {'phone':user_id}
#             updateObject = {'pagename':p_agename}
#             query = registartion.update_one(queryObject, {'$set': updateObject})
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#     else:
#         # queryObject = {'user_id':user_id, 'element_id':effect_id }
#         # updateObject = {'bookmark_time':datetime.now()}
#         # query = bookmarks.update_one(queryObject, {'$set': updateObject})
#         # print('update')
#         output["response"] = "taken"
#         return JSONEncoder().encode(output)


# @app.route('/registration/birthdate', methods=['POST'])
# def birthdate():
#     b_irthdate = request.values.get("birthdate")
#     user_id = request.values.get("user_id")
#     regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#     # query = collection.find()
#     # types = 'effect'
#     # bkmk = registartion.find_one({'email':email})
#     output = {}
#     if(re.search(regex, user_id)):
#         queryObject = {'email':user_id}
#         updateObject = {'birthdate':b_irthdate}
#         query = registartion.update_one(queryObject, {'$set': updateObject})
#         output["response"] = "verified"
#         return JSONEncoder().encode(output)
#     else:
#         queryObject = {'phone':user_id}
#         updateObject = {'birthdate':b_irthdate}
#         query = registartion.update_one(queryObject, {'$set': updateObject})
#         output["response"] = "verified"
#         return JSONEncoder().encode(output)
#     # return "Query Inserted!!"

# @app.route('/registration/password', methods=['POST'])
# def password():
#     p_assword = request.values.get("password")
#     user_id = request.values.get("user_id")
#     regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#     a = p_assword.encode("utf-8")
#     hashed = bcrypt.hashpw(a, bcrypt.gensalt(14))
#     print(hashed)
#     # query = collection.find()
#     # types = 'effect'
#     # bkmk = registartion.find_one({'email':email})
#     output ={}
#     if(re.search(regex, user_id)):
#         queryObject = {'email': user_id}
#         x123 = str(datetime.now())
#         print(x123)
#         updateObject = {'password':hashed, 'created_at':x123}
#         query = registartion.update_one(queryObject, {'$set': updateObject})
#         bkmk = registartion.find_one({'email':user_id})
#         bkmk2 = collection.find_one({'email':user_id})
#         if bkmk2 is None:
#             bkmk1 = collection.insert_one({ 'register_id':bkmk['_id'],'email':bkmk['email'], 'birthdate':bkmk['birthdate'], 'username':bkmk['username'], 'pagename':bkmk['pagename']})
#             print('update')
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#         else:
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#             # return "password Inserted!!"
#     else:
#         queryObject = {'phone':user_id}
#         updateObject = {'password':hashed, 'created_at':datetime.now()}
#         query = registartion.update_one(queryObject, {'$set': updateObject})
#         bkmk = registartion.find_one({'phone':user_id})
#         bkmk2 = collection.find_one({'phone':user_id})
#         if bkmk2 is None:
#             bkmk1 = collection.insert_one({ 'register_id':bkmk['_id'],'phone':bkmk['phone'], 'birthdate':bkmk['birthdate'], 'username':bkmk['username'], 'pagename':bkmk['pagename']})
#             print('update')
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#         else:
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)


# @app.route('/signIIn', methods=['POST'])
# def SignIn():
#     user_id = request.values.get("user_id")
#     print(user_id)
#     paassword = request.values.get("password")
#     a = paassword.encode("utf-8")
#     print(a)
#     print(paassword)
#     regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#     regex1 = "(0|91)?[7-9][0-9]{9}"
#     # obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
#     # message = b"The answer is no"
#     # print(message)
#     # ciphertext = obj.encrypt(message)
#     # print(ciphertext)


#     # passworda = "super secret password"
#     # print(passworda)
#     # hashed = bcrypt.hashpw(a, bcrypt.gensalt(14))
#     # print(hashed)
#     # hashed1 = b'$2b$14$KmJZ7KQRfj/rka5C5JI6p.hh20FyWGHNdEqDgT6pBFiHE4t.U19Vm'
#     # if bcrypt.checkpw(a, hashed1):
#     #     print("It Matches!")
#     # else:
#     #     print("It Does not Match :(")
#     # regex2  = "[7-9][0-9]{9}"
#     # query = collection.find()
#     # types = 'effect'
#     # bkmk = registartion.find_one({'email':email})
#     if(re.search(regex, user_id)):
#         bkmk = registartion.find_one({'email':user_id})
#         print(bkmk)
#         output = {}
#         abc = []
#         print(bkmk['password'])
#         if bcrypt.checkpw(a, bkmk['password']):
#             print("It Matches!")
#             bkmk = collection.find_one({'email':user_id})
#             # for x in bkmk:
#             #     print(x)
#             print(bkmk)
#             output["xyz"] = bkmk
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#         else:
#             print("It Does not Match :(")
#             output["response"] = "wrong password"
#             return JSONEncoder().encode(output)
#         # for x in bkmk:
#         #     abc.append(x)
#         #     print(x)
#         # print(abc)
#         # output["users"] = abc
#         # queryObject = {'email':e_mail}
#         # updateObject = {'password':p_assword}
#         # query = registartion.update_one(queryObject, {'$set': updateObject})
#         # return JSONEncoder().encode(output)
#     elif(re.search(regex1, user_id)):
#         bkmk = registartion.find_one({'phone':user_id})
#         output = {}
#         abc = []
#         print(bkmk)
#         # print(bkmk['password'])
#         if bcrypt.checkpw(a, bkmk['password']):
#             print("It Matches!")
#             bkmk = collection.find_one({'phone':user_id})
#             output["users"] = bkmk
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#         else:
#             print("It Does not Match :(")
#             output["response"] = "wrong password"
#             return JSONEncoder().encode(output)
#         # for x in bkmk:
#         #     abc.append(x)
#         # print(x)
#         # print(abc)
#         # output["users"] = abc
#         # # queryObject = {'email':e_mail}
#         # # updateObject = {'password':p_assword}
#         # # query = registartion.update_one(queryObject, {'$set': updateObject})
#         # return JSONEncoder().encode(output)
#     else:
#         bkmk = registartion.find_one({'username':user_id})
#         output = {}
#         abc = []
#         print(bkmk)
#         print(bkmk['password'])
#         if bcrypt.checkpw(a, bkmk['password']):
#             print("Its Matches!")
#             bkmk = collection.find_one({'username':user_id})
#             output["users"] = bkmk
#             output["response"] = "verified"
#             return JSONEncoder().encode(output)
#         else:
#             print("It Does not Match :(")
#             output["response"] = "wrong password"
#             return JSONEncoder().encode(output)
#         # queryObject = {'email':e_mail}
#         # updateObject = {'password':p_assword}
#         # query = registartion.update_one(queryObject, {'$set': updateObject})
#         # return JSONEncoder().encode(output)

# ################################################# Followers/Following #########################################################


# # @app.route('/folloewer/', methods=['POST'])
# # def follow():
# #     follower_id = request.values.get("follower_id")
# #     following_id = request.values.get("following_id")
# #     button_state = request.values.get("button_state")
# #     if button_state == 1:
# #         bkmk = collection.find_one({'follower_id': follower_id, 'following_id': following_id}) #follower table
# #         if bkmk is None:
# #             bkmk1 = collection.insert_one({'follower_id': follower_id, 'following_id': following_id}) #follower table
# #             print("followed")
# #             return "followed"
# #         else:
# #             print("user already followed")
# #             return "followed"
# #     else:
# #         bkmk = collection.find_one({'follower_id': follower_id, 'following_id': following_id}) #follower table
# #         if bkmk is None:
# #             bkmk1 = collection.delete_one({'follower_id': follower_id, 'following_id': following_id}) #follower table
# #             print("followed")
# #             return "followed"
# #         else:
# #             print("user already followed")
# #             return "followed"

#     # print(user_id)


# # @app.route('/getfollower', methods=['POST'])
# # def getfollower():
# #     user_id = request.values.get("user_id")
# #     bkmk = collection.find({'follower_id':user_id}) #follower table
# #     abc = []
# #     output={}
# #     for x in bkmk:
# #         abc.append(x)
# #     output["user"]  = abc
# #     return JSONEncoder().encode(output)


# @app.route('/following', methods=['POST'])
# def getfollowers():
#     user_id = request.values.get("user_id")
#     bkmk = collection.find({'follower_id':user_id}) #follower table
#     abc = []
#     output={}
#     for x in bkmk:
#         abc.append(x)
#     output["user"]  = abc
#     return JSONEncoder().encode(output)

#     # print(user_id)


# @app.route('/getfollowing', methods=['POST'])
# def getfollowing():
#     user_id = request.values.get("user_id")
#     bkmk = collection.find({'following_id':user_id}) #follower table
#     abc = []
#     output={}
#     for x in bkmk:
#         abc.append(x)
#     output["user"]  = abc
#     return JSONEncoder().encode(output)

#     print(user_id)


# ####################################################### Edit Profile ###########################################################

# @app.route('/editProfile', methods=['POST'])
# def editprofile():
#     user_id = request.values.get("user_id")
#     name = request.values.get("name")
#     bio = request.values.get("bio")
#     img = request.values.get("img")
#     url = request.values.get("url")
#     username = request.values.get("username")
#     output={}
#     # user_id1 = 'ObjectId("'+user_id+'")'
#     queryObject = {'_id': ObjectId(user_id)}
#     bkmk = collections.find({'username':username})
#     if bkmk is None:
#         updateObject = {'name': name, 'bio':bio, 'img': img, 'website':url, 'username':username}#{"age": 23}
#         query = collection.update_one(queryObject, {'$set': updateObject})
#         output["response"]  = "updated"
#         if query.acknowledged:
#             return "Update Successful"
#         else:
#             return "Update Unsuccessful"
#             # return JSONEncoder().encode(output)
#     else:
#         updateObject = {'name': name, 'bio':bio, 'img': img, 'website' :url} #{"age": 23}
#         query = collection.update_one(queryObject, {'$set': updateObject})
#         output["response"]  = "username exist!"
#         return JSONEncoder().encode(output)
#     # bkmk = collection.find({'_id':user_id}) #follower table

#     # abc = []
#     # output={}
#     # for x in bkmk:
#     #     abc.append(x)
        
# @app.route('/editProfilees', methods=['POST'])
# def editprofilees():
#     user_id = request.values.get("user_id")
#     name = request.values.get("name")
#     userid1 = '"'+user_id +'"'
#     print(ObjectId(user_id))
#     queryObject = {'_id': ObjectId(user_id)}
#     updateObject = {'nameeeeeee': name}#{"age": 23}
#     query = collection.update_one(queryObject, {'$set': updateObject})
#     if query.acknowledged:
#         return "Update Successful"
#     else:
#         return "Update Unsuccessful"


# ################################################### Notification ##############################################################


# @app.route('/Notification/Follower', methods=['POST'])
# def notifyFollower():
#     id = request.values.get("user_id") #following_id
#     id1 = ObjectId(id)
#     # print(len(values))
#     # # if len(values) == 0:
#     # #     output = {}
#     # #     print('*')
#     # # else:
#     # v1 = '.*'+values+'.*'
#     # rgx = re.compile(v1, re.IGNORECASE)
#     # print(rgx)
#     # queryObject = {"username": rgx}
#     # query = follower_table.find({"following_id": id}).sort('date',pymongo.DESCENDING)
#     query = follower_table.aggregate([
#         {"$match": {"following_id": id1}},
#         {"$sort": {"followed_time": -1}},
#         { "$lookup": {
#             'from': 'profile',
#             'localField': 'follower_id',
#             'foreignField': "_id",
#             'as': "userinfo"
#         } },
#         { "$unwind": "$userinfo" },
#         { "$project": {
#             "followed_time":1,
#             "userinfo._id": 1,
#             "userinfo.name": 1,
#             "userinfo.username":1
#         } }
#     ])
#     output = {}
#     abc = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x)
#         # print(x)
#     print(abc)
#     output["users"] = abc
#     output["response"] ="success"
#     return JSONEncoder().encode(output)



################################################# Followers/Following #########################################################



@app.route('/following', methods=['POST'])
def getfollowers():
    user_id = request.values.get("user_id")
    bkmk = collection.find({'follower_id':user_id}) #follower table
    abc = []
    output={}
    for x in bkmk:
        abc.append(x)
    output["user"]  = abc
    return JSONEncoder().encode(output)

    # print(user_id)


@app.route('/getfollowing', methods=['POST'])
def getfollowing():
    user_id = request.values.get("user_id")
    print(user_id)
    user_id1 = ObjectId(user_id)
    print(user_id1)
    # bkmk = follower_table.find({'following_id':user_id1}) #follower table
    query = follower_table.aggregate([
        {"$match": {"following_id": user_id1}},
        {"$sort": {"followed_time": -1}},
        { "$lookup": {
            'from': 'profile',
            'localField': 'follower_id',
            'foreignField': "_id",
            'as': "followeruserinfo"
        } },
        { "$unwind": "$followeruserinfo" },
        { "$project": {
            "followed_time":1,
            "followeruserinfo._id": 1,
            "followeruserinfo.name": 1,
            "followeruserinfo.username":1,
            "followeruserinfo.bio":1,
            "followeruserinfo.website":1
        } }
    ])
    abc = []
    output={}
    for x in query:
        abc.append(x)
    print(abc)
    output["hashtags"]  = abc
    return JSONEncoder().encode(output)






@app.route('/getfollower', methods=['POST'])
def getfollower():
    user_id = request.values.get("user_id")
    print(user_id)
    user_id1 = ObjectId(user_id)
    print(user_id1)
    # bkmk = follower_table.find({'following_id':user_id1}) #follower table
    query = follower_table.aggregate([
        {"$match": {"follower_id": user_id1}},
        {"$sort": {"followed_time": -1}},
        { "$lookup": {
            'from': 'profile',
            'localField': 'following_id',
            'foreignField': "_id",
            'as': "followeruserinfo"
        } },
        { "$unwind": "$followeruserinfo" },
        { "$project": {
            "followed_time":1,
            "followeruserinfo._id": 1,
            "followeruserinfo.name": 1,
            "followeruserinfo.username":1,
            "followeruserinfo.bio":1,
            "followeruserinfo.website":1
        } }
    ])
    abc = []
    output={}
    for x in query:
        abc.append(x)
    print(abc)
    output["hashtags"]  = abc
    return JSONEncoder().encode(output)

    print(user_id)


####################################################### Edit Profile ###########################################################

@app.route('/editProfile', methods=['POST'])
def editprofile():
    user_id = request.values.get("user_id")
    name = request.values.get("name")
    bio = request.values.get("bio")
    img = request.values.get("img")
    url = request.values.get("url")
    username = request.values.get("username")
    output={}
    # user_id1 = 'ObjectId("'+user_id+'")'
    queryObject = {'_id': ObjectId(user_id)}
    bkmk = collections.find({'username':username})
    if bkmk is None:
        updateObject = {'name': name, 'bio':bio, 'img': img, 'website':url, 'username':username}#{"age": 23}
        query = collection.update_one(queryObject, {'$set': updateObject})
        output["response"]  = "updated"
        if query.acknowledged:
            return "Update Successful"
        else:
            return "Update Unsuccessful"
            # return JSONEncoder().encode(output)
    else:
        updateObject = {'name': name, 'bio':bio, 'img': img, 'website' :url} #{"age": 23}
        query = collection.update_one(queryObject, {'$set': updateObject})
        output["response"]  = "username exist!"
        return JSONEncoder().encode(output)
    # bkmk = collection.find({'_id':user_id}) #follower table

    # abc = []
    # output={}
    # for x in bkmk:
    #     abc.append(x)



   #############error #############333     
@app.route('/editProfilees', methods=['POST'])
def editprofilees():
    user_id = request.values.get("user_id")
    name = request.values.get("name")
    userid1 = '"'+user_id +'"'
    print(ObjectId(user_id))
    queryObject = {'_id': ObjectId(user_id)}
    updateObject = {'nameeeeeee': name}#{"age": 23}
    query = collection.update_one(queryObject, {'$set': updateObject})
    if query.acknowledged:
        return "Update Successful"
    else:
        return "Update Unsuccessful"


################################################### Notification ##############################################################


@app.route('/Notification/Follower', methods=['POST'])
def notifyFollower():
    id = request.values.get("user_id") #following_id
    id1 = ObjectId(id)
    # print(len(values))
    # # if len(values) == 0:
    # #     output = {}
    # #     print('*')
    # # else:
    # v1 = '.*'+values+'.*'
    # rgx = re.compile(v1, re.IGNORECASE)
    # print(rgx)
    # queryObject = {"username": rgx}
    # query = follower_table.find({"following_id": id}).sort('date',pymongo.DESCENDING)
    query = follower_table.aggregate([
        {"$match": {"following_id": id1}},
        {"$sort": {"followed_time": -1}},
        { "$lookup": {
            'from': 'profile',
            'localField': 'follower_id',
            'foreignField': "_id",
            'as': "userinfo"
        } },
        { "$unwind": "$userinfo" },
        { "$project": {
            "followed_time":1,
            "userinfo._id": 1,
            "userinfo.name": 1,
            "userinfo.username":1
        } }
    ])
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        # print(x)
    print(abc)
    output["users"] = abc
    output["response"] ="success"
    return JSONEncoder().encode(output)




@app.route('/Notification/Mention', methods=['POST'])
def notifyMention():
    username = request.values.get("username") #username
    # id1 = ObjectId(id)
    output={}
    # query = collections.find({"mention_friends":{"$in":[username]}})
    # print("username")
    query = collections.aggregate([
        {"$match": {"mention_friends":{"$in":[username]}}},
        {"$sort": {"created_at": -1}},
        { "$lookup": {
            'from': 'profile',
            'localField': 'username',
            'foreignField': "username",
            'as': "userinfo"
        } },
        { "$unwind": "$userinfo" },
        { "$project": {
            "created_at":1,
            "userinfo.purl":1,
            "username":1,
            "img_url":1,
            "caption":1,
            "location":1,
            "mention_friends":1

        } }
    ])
    abc = []
    for x in query:
        print(x)
        abc.append(x)
    output["videodetailss"] = abc
    return JSONEncoder().encode(output)






@app.route('/Notification/Swipeup', methods=['POST'])
def notifyswipeup():
    username = request.values.get("username") #username
    # id1 = ObjectId(id)
    output={}
    # query = collections.find({"mention_friends":{"$in":[username]}})
    # print("username")
    query = collections.aggregate([
        {"$match": {"mention_friends":{"$in":[username]}}},
        {"$sort": {"created_at": -1}},
        { "$lookup": {
            'from': 'profile',
            'localField': 'username',
            'foreignField': "username",
            'as': "userinfo"
        } },
        { "$unwind": "$userinfo" },
        { "$project": {
            "created_at":1,
            "userinfo.purl":1,
            "username":1,
            "img_url":1,
            "caption":1,
            "location":1,
            "mention_friends":1


        } }
    ])
    abc = []
    for x in query:
        print(x)
        abc.append(x)
    output["videodetailss"] = abc
    return JSONEncoder().encode(output)




##########################################  Postvideo api ######################################################################
@app.route('/PostVideos', methods=['POST'])
def postVideos():
    video_url=request.values.get("video_url")
    img_url = request.values.get("img_url")
    caption =request.values.get("caption")
    mention =request.values.get("mention")
    hashtag=[]
    hashtag=re.findall(r'#[\w\.-]+',caption,flags=re.IGNORECASE),
    print(hashtag)
    video_privacy=request.values.get("video_privacy")
    allow_comment=request.values.get("allow_comment")
    allow_duet=request.values.get("allow_duet")
    save_to_device =request.values.get("save_to_device")
    user_id =request.values.get("user_id")
    print("xyz")
    output = {}   

    queryObject = {
                   'user_id':user_id,
                   'video_url':video_url,
                  'img_url':img_url,
                  'caption':caption,
                  'mention':mention,
                  'hashtag':hashtag,
                  'video_privacy':video_privacy,
                  'allow_comment':allow_comment,
                  'allow_duet':allow_duet,
                  'save_to_device':save_to_device,
                  'post_time':datetime.now() 
                  }

    query =postt.insert_one(queryObject)
    output['response'] = 'request_accept'
    return JSONEncoder().encode(output)

   

####################################### Upload Storage ########################

@app.route('/onVideocall', methods=['POST'])
def onVideocall():
    friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    output={}
    query =videocall.insert_one({"Outgoing": friendUsername, "Incoming": username})
    print(query)
    output['response'] = "requested"
    return JSONEncoder().encode(output)



@app.route('/checkIsavailable', methods=['POST'])
def checkisavailable():
    friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    output={}
    abc = "null"
    query =videocall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
    print(query)
    if query is None:
        print("None")
    else:
        # if query["IsAvailable"]:
        #     print("true")
        # else:
        #     print("false")
        for x in (query):
            print(x)
            if x == "IsAvailable":
                print("true")
                print(query["IsAvailable"])
                abc = query["IsAvailable"]
            print("***")
        output["response"] = "requested!!"
        output["IsAvailable"] = abc
    return  JSONEncoder().encode(output)


@app.route('/checkIfConnected', methods=['POST'])
def checkIfConnected():
    friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    output={}
    abc = "null"
    xyz = "null"
    query =videocall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
    print(query)
    if query is None:
        print("None")
    else:
        # if query["IsAvailable"]:
        #     print("true")
        # else:
        #     print("false")
        for x in (query):
            print(x)
            if x == "IsAvailable":
                print("true")
                print(query["IsAvailable"])
                abc = query["IsAvailable"]
            if x == "ConnectionID":
                print(query["ConnectionID"])
                xyz = query["ConnectionID"]
            print("***")
        output["response"] = "requested!!"
        output["IsAvailable"] = abc
        output["ConnectionID"] = xyz
    return  JSONEncoder().encode(output)




@app.route('/checkforIncoming', methods=['POST'])
def checkforIncomg():
    friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    query =videocall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
    output = {}
    if query is None:
        output["response"] = "nocall"
    else:
        output["response"] = "Calling"
    # print(query)
    return JSONEncoder().encode(output)


@app.route('/onCallRequest', methods=['POST'])
def onCallRequest():
    friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    queryObject = {"Outgoing": friendUsername, "Incoming": username}
    abc = int(random.randint(1000000000,9999999999))
    updateObject = {'ConnectionID': abc, "IsAvailable": True }
    query =videocall.update_one(queryObject, {'$set': updateObject})
    output = {}
    output["response"] = "Call Accepted!"
    return JSONEncoder().encode(output)


@app.route('/onCallReject', methods=['POST'])
def onCallReject():
    friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    queryObject = {"Outgoing": friendUsername, "Incoming": username}
    abc = int(random.randint(1000000000,9999999999))
    updateObject = {"Incoming": "null" }
    query =videocall.update_one(queryObject, {'$set': updateObject})
    output = {}
    output["response"] = "Call Rejected!"
    return JSONEncoder().encode(output)

@app.route('/onCallRejected', methods=['POST'])
def onCallRejected():
    friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    query =videocall.delete_one({"Outgoing": friendUsername, "Incoming": username})
    output = {}
    output["response"] = "Call Rejected!"
    return JSONEncoder().encode(output)

@app.route('/onCallcheckResponse', methods=['POST'])
def onCallcheckResponse():
    # friendUsername = request.values.get("friendUsername")
    username = request.values.get("username")
    # query = videoCall.delete_one({"Outgoing": friendUsername, "Incoming": username})
    query_object = {"Incoming": username}
    # query = []
    query =videocall.watch([{"$match": query_object}])
    output = {}
    print(query)
    for x in query:
        print(x)
    output["response"] = query
    return JSONEncoder().encode(output)


############################################ User Videos ###################################


@app.route('/UserVideos', methods=['POST'])
def userVideos():
    values = request.values.get("username") 
    queryObject = {"username": values, "type": "open"}
    query = collections.find(queryObject)
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["videos"] = abc
    return JSONEncoder().encode(output)


@app.route('/UserVideosLock', methods=['POST'])
def userVideosLock():
    values = request.values.get("username") 
    queryObject = {"username": values, "type":"lock"}
    query = collections.find(queryObject)
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["videos"] = abc
    return JSONEncoder().encode(output)



@app.route('/UserVideosFavourite', methods=['POST'])
def userVideosFavourite():
    values = request.values.get("username") 
    queryObject = {"username": values, "type":"favourite"}
    query = collections.find(queryObject)
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["videos"] = abc
    return JSONEncoder().encode(output)


#####################################  bookmark hashtags Videos ##############################

@app.route('/bookmarkHastagVideoss', methods=['POST'])
def bookmarkHastagVideos():
    # user_id = request.values.get("user_id")
    hashtag = request.values.get("hashtags")
    # print(user_id)
    # user_id1 = ObjectId(user_id)
    print(hashtag)
    query = collections.find({"hastag":{"$in":[hashtag]}})
    abc = []
    output = {}
    # print(query)
    for x in query:
        abc.append(x)
        print("*")
        print(x)
        print("*")
    print(abc)
    output['videos'] = abc
    return JSONEncoder().encode(output)


@app.route('/bookmarkSoundVideos', methods=['POST'])
def bookmarkSoundVideos():
    # user_id = request.values.get("user_id")
    song = request.values.get("songs")
    # print(user_id)
    # user_id1 = ObjectId(user_id)
    print(song)
    query = collections.find({"songs":song})
    abc = []
    output = {}
    # print(query)
    for x in query:
        abc.append(x)
        print("*")
        print(x)
        print("*")
    print(abc)
    output['videos'] = abc
    return JSONEncoder().encode(output)


####################################### User View Video ###################################


@app.route('/UserVideosView', methods=['POST'])
def userVideosView():
    values = request.values.get("username") 
    queryObject = {"username": values, "type": "open"}
    query = collections.find(queryObject)
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["videos"] = abc
    return JSONEncoder().encode(output)



@app.route('/UserVideosViewFavourite', methods=['POST'])
def userVideosViewFavourite():
    values = request.values.get("username") 
    queryObject = {"username": values, "type": "favourite"}
    query = collections.find(queryObject)
    output = {}
    abc = []
    i = 0
    print(query)
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output["videos"] = abc
    return JSONEncoder().encode(output)




####################################### Upload Storage #########################################




# @app.route('/onVideocall', methods=['POST'])
# def onVideocall():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     output={}
#     query = videoCall.insert_one({"Outgoing": friendUsername, "Incoming": username})
#     print(query)
#     output['response'] = "requested"
#     return JSONEncoder().encode(output)


# @app.route('/checkIsavailable', methods=['POST'])
# def checkisavailable():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     output={}
#     abc = "null"
#     query =videoCall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
#     print(query)
#     if query is None:
#         print("None")
#     else:
#         # if query["IsAvailable"]:
#         #     print("true")
#         # else:
#         #     print("false")
#         for x in (query):
#             print(x)
#             if x == "IsAvailable":
#                 print("true")
#                 print(query["IsAvailable"])
#                 abc = query["IsAvailable"]
#             print("***")
#         output["response"] = "requested!!"
#         output["IsAvailable"] = abc
#     return  JSONEncoder().encode(output)


# @app.route('/checkIfConnected', methods=['POST'])
# def checkIfConnected():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     output={}
#     abc = "null"
#     xyz = "null"
#     query = videoCall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
#     print(query)
#     if query is None:
#         print("None")
#     else:
#         # if query["IsAvailable"]:
#         #     print("true")
#         # else:
#         #     print("false")
#         for x in (query):
#             print(x)
#             if x == "IsAvailable":
#                 print("true")
#                 print(query["IsAvailable"])
#                 abc = query["IsAvailable"]
#             if x == "ConnectionID":
#                 print(query["ConnectionID"])
#                 xyz = query["ConnectionID"]
#             print("***")
#         output["response"] = "requested!!"
#         output["IsAvailable"] = abc
#         output["ConnectionID"] = xyz
#     return  JSONEncoder().encode(output)




# @app.route('/checkforIncoming', methods=['POST'])
# def checkforIncomg():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     query = videoCall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
#     output = {}
#     if query is None:
#         output["response"] = "nocall"
#     else:
#         output["response"] = "Calling"
#     # print(query)
#     return JSONEncoder().encode(output)


# @app.route('/onCallRequest', methods=['POST'])
# def onCallRequest():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     queryObject = {"Outgoing": friendUsername, "Incoming": username}
#     abc = int(random.randint(1000000000,9999999999))
#     updateObject = {'ConnectionID': abc, "IsAvailable": True }
#     query = videoCall.update_one(queryObject, {'$set': updateObject})
#     output = {}
#     output["response"] = "Call Accepted!"
#     return JSONEncoder().encode(output)


# @app.route('/onCallReject', methods=['POST'])
# def onCallReject():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     queryObject = {"Outgoing": friendUsername, "Incoming": username}
#     abc = int(random.randint(1000000000,9999999999))
#     updateObject = {"Incoming": "null" }
#     query = videoCall.update_one(queryObject, {'$set': updateObject})
#     output = {}
#     output["response"] = "Call Rejected!"
#     return JSONEncoder().encode(output)

# @app.route('/onCallRejected', methods=['POST'])
# def onCallRejected():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     query = videoCall.delete_one({"Outgoing": friendUsername, "Incoming": username})
#     output = {}
#     output["response"] = "Call Rejected!"
#     return JSONEncoder().encode(output)

# @app.route('/onCallcheckResponse', methods=['POST'])
# def onCallcheckResponse():
#     # friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     # query = videoCall.delete_one({"Outgoing": friendUsername, "Incoming": username})
#     query_object = {"Incoming": username}
#     # query = []
#     query = videoCall.watch([{"$match": query_object}])
#     output = {}
#     print(query)
#     for x in query:
#         print(x)
#     output["response"] = query
#     return JSONEncoder().encode(output)


# ############################################ User Videos ###################################


# @app.route('/UserVideos', methods=['POST'])
# def userVideos():
#     values = request.values.get("username") 
#     queryObject = {"username": values, "type": "open"}
#     query = collections.find(queryObject)
#     output = {}
#     abc = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x)
#         print(x)
#     print(abc)
#     output["videos"] = abc
#     return JSONEncoder().encode(output)


# @app.route('/UserVideosLock', methods=['POST'])
# def userVideosLock():
#     values = request.values.get("username") 
#     queryObject = {"username": values, "type":"lock"}
#     query = collections.find(queryObject)
#     output = {}
#     abc = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x)
#         print(x)
#     print(abc)
#     output["videos"] = abc
#     return JSONEncoder().encode(output)



# @app.route('/UserVideosFavourite', methods=['POST'])
# def userVideosFavourite():
#     values = request.values.get("username") 
#     queryObject = {"username": values, "type":"favourite"}
#     query = collections.find(queryObject)
#     output = {}
#     abc = []
#     i = 0
#     print(query)
#     for x in query:
#         abc.append(x)
#         print(x)
#     print(abc)
#     output["videos"] = abc
#     return JSONEncoder().encode(output)





####################################### Upload Storage #########################################

# @app.route('/onVideocall', methods=['POST'])
# def onVideocall():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     output={}
#     query = videocall.insert_one({"Outgoing": friendUsername, "Incoming": username})
#     print(query)
#     output['response'] = "requested"
#     return JSONEncoder().encode(output)


# @app.route('/checkIsavailable', methods=['POST'])
# def checkisavailable():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     output={}
#     abc = "null"
#     query =videocall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
#     print(query)
#     if query is None:
#         print("None")
#     else:
#         # if query["IsAvailable"]:
#         #     print("true")
#         # else:
#         #     print("false")
#         for x in (query):
#             print(x)
#             if x == "IsAvailable":
#                 print("true")
#                 print(query["IsAvailable"])
#                 abc = query["IsAvailable"]
#             print("***")
#         output["response"] = "requested!!"
#         output["IsAvailable"] = abc
#     return  JSONEncoder().encode(output)


# @app.route('/checkIfConnected', methods=['POST'])
# def checkIfConnected():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     output={}
#     abc = "null"
#     xyz = "null"
#     query = videocall.find_one({"Outgoing": friendUsername, "Incoming": username}) #Requested table
#     print(query)
#     if query is None:
#         print("None")
#     else:
#         # if query["IsAvailable"]:
#         #     print("true")
#         # else:
#         #     print("false")
#         for x in (query):
#             print(x)
#             if x == "IsAvailable":
#                 print("true")
#                 print(query["IsAvailable"])
#                 abc = query["IsAvailable"]
#             if x == "ConnectionID":
#                 print(query["ConnectionID"])
#                 xyz = query["ConnectionID"]
#             print("***")
#         output["response"] = "requested!!"
#         output["IsAvailable"] = abc
#         output["ConnectionID"] = xyz
#     return  JSONEncoder().encode(output)




# @app.route('/checkforIncoming', methods=['POST'])
# def checkforIncomg():
#     # friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     query =videocall.find_one({"Incoming": username}) #Requested table
#     output = {}
#     if query is None:
#         output["response"] = "nocall"
#     else:
#         output["callerName"] = query["Outgoing"]
#         output["response"] = "Calling"
#     # print(query)
#     return JSONEncoder().encode(output)


# @app.route('/onCallRequest', methods=['POST'])
# def onCallRequest():
#     # friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     queryObject = { "Incoming": username}
#     abc = int(random.randint(1000000000,9999999999))
#     updateObject = {'ConnectionID': abc, "IsAvailable": True }
#     query = videocall.update_one(queryObject, {'$set': updateObject})
#     output = {}
#     output["response"] = "Call Accepted!"
#     return JSONEncoder().encode(output)


# @app.route('/onCallReject', methods=['POST'])
# def onCallReject():
#     # friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     queryObject = {"Incoming": username}
#     abc = int(random.randint(1000000000,9999999999))
#     updateObject = {"Incoming": "null" }
#     query = videocall.update_one(queryObject, {'$set': updateObject})
#     output = {}
#     output["response"] = "Call Rejected!"
#     return JSONEncoder().encode(output)

# @app.route('/onCallRejected', methods=['POST'])
# def onCallRejected():
#     friendUsername = request.values.get("friendUsername")
#     username = request.values.get("username")
#     query =videocall.delete_one({"Outgoing": friendUsername, "Incoming": username})
#     output = {}
#     output["response"] = "Call Rejected!"
#     return JSONEncoder().encode(output)


######################################### follower/ following count ##############################

@app.route('/follower&followingcount', methods=['POST'])
def followerfollowingcount():
    user_id = request.values.get("user_id")
    user_id1 = ObjectId(user_id)
    following_count = follower_table.find({'following_id':user_id1}).count()
    follower_count =  follower_table.find({'follower_id':user_id1}).count()
    # print(bkmk)
    output={}
    output["follower_count"] = follower_count
    output["following_count"] = following_count
    return JSONEncoder().encode(output)


if __name__ == '__main__':
    app.debug = True
    app.run()


######################################## post API ##################################

# @app.route('/post', methods=['POST'])
# def post():
#     video_url=request.values.get("video_url")
# img_url=request.values.get("img_url")
# caption=request.values.get("caption")
# mention=request.values.get("mention")         
# hastag=request.values.get("hastag")
# video_privacy=request.values.get("video_privacy")
# allow_comment=request.values.get("allow_comment")
# allow_duet=request.values.get("allow_duet")

# queryObject = {
#                'video_url':video_url,
#                 'img_url':img_url,
#                 'caption':caption,
#                 'mention':mention,
#                 'hastag':hastag,
#                 'video_privacy':video_privacy,
#                 'allow_comment':allow_comment,
#                 'allow_duet':allow_duet }

# query =post.insert_on(queryObject)
# return "Query Inserted!!"




# @app.route('/postt', methods=['POST'])
# def postt():
#     videourl = request.values.get("videourl")
#     imgurl = request.values.get("imgurl")
#     caption =request.values.get("caption")
#     mention =request.values.get("mention")
#     hastag=request.values.get("hastag")
#     video_privacy=request.values.get("video_privacy")
#     allow_comment=request.values.get("allow_comment")
#     allow_duet=request.values.get("allow_duet")

    
#     queryObject = {
#                 'video_url':videourl,
#                 'img_url':imgurl,
#                  'caption':caption,
#                  'mention':mention,
#                  'hastag':hastag,
#                  'video_privacy':video_privacy,
#                  'allow_comment':allow_comment,
#                  'allow_duet':allow_duet }

#     query =postt.insert_on(queryObject)
#     return "Query Inserted!!"


############## POST VIDEO API #############################################

@app.route('/PostVideos', methods=['POST'])
def postVideos():
    username = request.values.get("username")
    video_url =request.values.get("video_url")
    img_url=request.values.get("img_url")
    caption=request.values.get("caption")
    mention=request.values.get("mention")
    hashtag=[]
    hashtag=re.findall(r'#[\w\.-]+',caption,flags=re.IGNORECASE),
    print(hashtag)
    video_privacy=request.values.get("video_privacy")
    allow_comment=request.values.get("allow_comment")
    allow_duet=request.values.get("allow_duet")
    save_to_device=request.values.get("save_to_device")
    user_id=request.values.get("user_id")
    output={}
    x=datetime.now()
    user_id1=ObjectId(user_id)
    
    queryObject = {
                   'username':username,
                   'created_at':str(x),
                   'user_id':user_id1,
                   'img_url':video_url,
                   'video_url':img_url,
                   'caption':caption,
                   'mention_friends':mention,
                   'hashtag':hashtag,
                   'video_privacy':video_privacy,
                   'allow_duet':allow_duet,
                   'save_to_device':save_to_device,
                   
                   }


    query =collections.insert_one(queryObject)
    output['response'] = 'request_accept'
    return JSONEncoder.encode(output)




    ###################################### HOME Video Api #############################




@app.route('/home/videos', methods=['POST'])
def homeVideos():
    user_id = request.values.get("user_id")
    print(user_id)
    user_id1 = ObjectId(user_id)
    query = follower_table.aggregate([
            {"$match": {"following_id": user_id1}},
            { "$lookup": {
                'from': 'videos',
                'localField': 'follower_id',
                'foreignField': "user_id",
                'as': "videoinfo"
            } },
            { "$unwind": "$videoinfo" },
            { "$project": {
                "following_id":1,
                "follower_id":1,
                "videoinfo.user_id":1,
                "videoinfo.created_at":1,
                "videoinfo.caption":1,
                "videoinfo._id": 1,
                "videoinfo.username": 1,
                "videoinfo.img_url":1
            } }
        ])
    abc = []
    output = {}
    for x in query:
        abc.append(x)
        print(x)
    print(abc)
    output['videos'] = abc
    return JSONEncoder().encode(output)

#################### Follower / following count ########################



@app.route('/follower&followingcount', methods=['POST'])
def followerfollowingcount():
    user_id = request.values.get("user_id")
    user_id1 = ObjectId(user_id)
    following_count = follower_table.find({'following_id':user_id1}).count()
    follower_count =  follower_table.find({'follower_id':user_id1}).count()
    # print(bkmk)
    output={}
    output["follower_count"] = follower_count
    output["following_count"] = following_count
    return JSONEncoder().encode(output)



if __name__ == '__main__':
    app.debug = True
    app.run()
<<<<<<< HEAD




################################## chat ####################################



# @app.route('/chatdb', methods=['POST'])
# def chat():
#     senderid = request.values.get("senderid")
#     receiverid = request.values.get("receiverid")
#     roomid = senderid+receiverid
#     x = datetime.now()
#     querry = chat_db.find_one({'senderid': senderid, 'receiverid': receiverid, 'roomid':roomid})
#     if querry is None:
#         query2 = {'senderid': senderid, 'receiverid': receiverid, 'roomid':roomid, 'timestamp': str(x)}
#         query = chat_db.insert_one(query2)
#         print("added")
#     else:
#         print(querry)
#         updateObject = {'timestamp': str(x)} 
#         query1 = {'senderid': senderid, 'receiverid': receiverid, 'roomid':roomid}
#         updatee = chat_db.update_one(query1, {'$set': updateObject})
#         print("updated")
#     output = {}
#     output["response"] = "Successfull"
#     return JSONEncoder().encode(output)

#     # return



# @app.route('/chatsActivity', methods=['POST'])
# def chatsActivity():
#     senderid = request.values.get("senderid")
#     print(senderid)
#     querry = chat_db.aggregate([
#         {'$match' :{"senderid":senderid}},
#         {'$sort':{"timestamp": -1}}
#         ])
#     abc=[]
#     for x in querry:
#         print(x)
#         abc.append(x)
#     output = {}
#     output["chatuserss"] = abc
#     return JSONEncoder().encode(output)



# if __name__ == '__main__':
#     app.debug = True
#     app.run()
=======
>>>>>>> c99cb4a20b85d6dad1254b8480d0ee43f52d7693
