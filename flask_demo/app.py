from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask import json
from bson.json_util import dumps
from bson.objectid import ObjectId
from operator import itemgetter
import pprint

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')

# Connecting to a DB
db = client.Trains

# Getting a collection
Train = db.Train


# Hello World Route
@app.route('/')
def hello_world():
    return jsonify(message='Hello from Flask Server', API='http://localhost:5000/api/trains/doc')


# GET: All Trains
@app.route('/api/trains', methods=['GET'])
def getAllTrains():
    allTrains = Train.find({})
    res = dumps(allTrains)
    return res


# GET: One Train
@app.route('/api/trains/<id>', methods=['GET'])
def getOneTrain(id):
    train = Train.find_one({'_id': ObjectId(id)})
    res = dumps(train)
    return res


# POST: Create new train
@ app.route('/api/trains', methods=['POST'])
def createNewTrain():
    req = request.json
    name = req['name']
    description = req['description']
    distance_between_stop = req['distance-between-stop']
    max_speed = req['max-speed']
    sharing_tracks = req['sharing-tracks']
    grade_crossing = req['grade-crossing']
    train_frequency = req['train-frequency']
    amenities = req['amenities']
    newTrain = {'name': name, 'description': description, 'distance-between-stop': distance_between_stop, 'max-speed': max_speed,
                'sharing-tracks': sharing_tracks, 'grade-crossing': grade_crossing, 'train_frequency': train_frequency, 'amenities': amenities}
    print(newTrain)

    if name and description and distance_between_stop and max_speed and sharing_tracks and grade_crossing and train_frequency and amenities and request.method == 'POST':
        print('All values are there')
        Train.insert_one(newTrain)
    else:
        return not_found()

    return jsonify('New User Created!!!')


# DELETE: Delete train
@app.route('/api/trains/<id>', methods=['DELETE'])
def deleteTrain(id):
    trainToDelete = Train.find_one({'_id': ObjectId(id)})
    if trainToDelete:
        Train.delete_one({'_id': ObjectId(id)})
        return jsonify(message='Train Successfully Deleted!!')
    else:
        return 'train with given ID not found'


# PUT: Update the train
@app.route('/api/trains/<id>', methods=['PUT'])
def updateTrain(id):
    oldTrain = Train.find_one({'_id': ObjectId(id)})
    if oldTrain:
        print('Train Found')
    else:
        return 'train with given ID not found'

    req = request.json
    print(oldTrain)

    try:
        name = req['name']
        description = req['description']
        distance_between_stop = req['distance-between-stop']
        max_speed = req['max-speed']
        sharing_tracks = req['sharing-tracks']
        grade_crossing = req['grade-crossing']
        train_frequency = req['train-frequency']
        amenities = req['amenities']

    except Exception as e:
        name = oldTrain['name']
        description = oldTrain['description']
        distance_between_stop = oldTrain['distance-between-stop']
        max_speed = oldTrain['max-speed']
        sharing_tracks = oldTrain['sharing-tracks']
        grade_crossing = oldTrain['grade-crossing']
        train_frequency = oldTrain['train-frequency']
        amenities = oldTrain['amenities']
        if name and description and distance_between_stop and max_speed and sharing_tracks and grade_crossing and train_frequency and amenities and request.method == 'PUT':
            print('All values are there')
            Train.update_one({"_id": ObjectId(id)}, {"$set":  {'name': name, 'description': description, 'distance-between-stop': distance_between_stop,
                                                               'max-speed': max_speed, 'sharing-tracks': sharing_tracks, 'grade-crossing': grade_crossing, 'train_frequency': train_frequency, 'amenities': amenities}})
            return jsonify("Train successfully Updated")
        else:
            return not_found()


# ERROR: Error handler
@ app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }
    resp = jsonify(message)
    return resp


print('Flask server is running on http://localhost:5000')
# name = req['name']
# description = req['description']
# distance_between_stop = req['distance-between-stop']
# max_speed = req['max-speed']
# sharing_tracks = req['sharing-tracks']
# grade_crossing = req['grade-crossing']
# train_frequency = req['train-frequency']
# amenities = req['amenities']

# if name and description and distance_between_stop and max_speed and sharing_tracks and grade_crossing and train_frequency and amenities and request.method == 'POST':
#     query = {'_id': ObjectId(id)}
#     newValues = {"$set": {"name": name, "description": description, "distance-between-stop": distance_between_stop, "max-speed": max_speed,
#                           "sharing-tracks": sharing_tracks, "grade-crossing": grade_crossing, "train-frequency": train_frequency, "amenities": amenities}}
#     return 'Train Successfully Updated!!!'
#     # Train.update_one(query, newValues)
# else:
#     return not_found()
