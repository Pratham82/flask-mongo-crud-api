# flask-mongo-crud-api
Flask + MongoDB CRUD API

### Required Packages:

```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
py-mon==1.0.2
pymongo==3.11.3
Werkzeug==1.0.1
```

### Usage
Use [potery](https://python-poetry.org/) for installing packages using poetry
```
poetry install
```
**Optional** Enable poetry shell(this is similar to **virtual environment/pienv**)
```
poetry shell 
```

####  You can run the application in 2 ways:

Go to flask-demo 
```
cd flask_demo
```

Using **flask run**
```
flask run 
```

Using custom **debug script** this script will **reload** the **flask server every time there is a change** in the application

Change file permissions for executing
```
chmod u+x ./debug.sh
```
Run debug script
```
./debug.sh
```

## Mongo setup
Run mongodb
```
mongod
```

Create Database named Trains:
```
create databse Trains
```

Create Train collection:
```
db.createCollections('Train')
```

Create new Train:
```
db.Train.insert({
   "name":"T1",
   "description":"This is T1",
   "distance-between-stop":"2km",
   "max-speed":"35km/hr",
   "sharing-tracks":true,
   "grade-crossing":true,
   "train-frequency":"2/hr",
   "amenities":"AC"
})
```


## API Documentation 

Use POSTMAN or Insomnia for testing the API:

We are working with Train model here, following is the model schema
```
{
 id: number
 name: string
 description: string
 distance-between-stop: string
 max-speed: string
 sharing-tracks: boolean
 grade-crossing: boolean
 train-frequency: string
 amenities: string 
 }
```

### Routes

**GET**

This route will give you all the trains
```
localhost:5000/api/trains/
```


**GET ONE**

This route will give you the train with the provided ID

```
localhost:5000/api/trains/:id
```

**POST**

Creating new train with the given Request body in JSON
```
localhost:5000/api/trains/
```
Eg. Request body
```
{
   "name":"T3",
   "description":"This is T3",
   "distance-between-stop":"4km",
   "max-speed":"7km/hr",
   "sharing-tracks":true,
   "grade-crossing":true,
   "train-frequency":"2/hr",
   "amenities":"AC"
}

```

**DELETE**

This route will delete the train with the provided ID

```
localhost:5000/api/trains/:id
```


**UPDATE**

This route will update the train with the provided ID and given Request body in JSON

```
localhost:5000/api/trains/:id
```

