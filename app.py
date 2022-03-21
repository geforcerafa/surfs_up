# Import dependencies 
import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import dependencies we need from Flask
from flask import Flask, jsonify

# Set up the database enginne for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the Database into our clases
Base = automap_base()

# Reflect the Database
Base.prepare(engine, reflect=True)

# save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Define our Flask app, add the following line of code. 
# # This will create a Flask application called "app."
app = Flask(__name__)

# Define the welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#### Every time you create a new route,
####  your code should be aligned all the way to the left
#### in order to avoid errors

## Create a route for the prcipitation analysis
# calculates the date one year ago from the most recent date in the database
# write a query to get the date and precipitation for the previous year
# Create a dictionary with the date as the key and
#    the precipitation as the value
# To create the dictionay JSONIFY our dictionary, convert it to json
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# en Anaconda Powershell prompt (Phyton Data)
# Vas al forlder del archivo, luego Codigo para correr Flask : 
# set FLASK_APP=app.py
# flask run
# http://127.0.0.1:5000/ = http://localhost:5000/

#Third route, stations 
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Temperature Observations from last year, first the route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Min, Max and Avg temp 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)