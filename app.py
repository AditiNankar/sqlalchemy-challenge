from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import json

# Setup the database connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)
Session = Session(engine)

# Reference to the tables
Measurement = Base.classes.measurement
Stations = Base.classes.station

# Initialize Flask app
app = Flask(__name__)

# Home route - List all available routes
@app.route('/')
def home():
    return (
        """
        <h1>Welcome to the Climate API</h1>
        <p>Available Routes:</p>
        <ul>
            <li>/api/v1.0/precipitation</li>
            <li>/api/v1.0/stations</li>
            <li>/api/v1.0/tobs</li>
            <li>/api/v1.0/&lt;start&gt;</li>
            <li>/api/v1.0/&lt;start&gt;/&lt;end&gt;</li>
        </ul>
        """
    )

# /api/v1.0/precipitation - Get last 12 months of precipitation data
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Calculate the date one year ago
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Query the last 12 months of precipitation data
    precip_data = (
        session.query(Measurement.date, Measurement.prcp)
        .filter(Measurement.date >= one_year_ago)
        .order_by(Measurement.date)
        .all()
    )
    
    # Convert query results to a dictionary
    precip_dict = {date: prcp for date, prcp in precip_data}
    
    return jsonify(precip_dict)

# /api/v1.0/stations - Get list of all stations
@app.route('/api/v1.0/stations')
def stations():
    # Query to get all station IDs
    stations_data = session.query(Stations.station).all()
    
    # Convert the list of tuples to a list of station IDs
    stations_list = [station[0] for station in stations_data]
    
    return jsonify(stations_list)

# /api/v1.0/tobs - Get temperature observations for the most active station
@app.route('/api/v1.0/tobs')
def tobs():
    # Find the most active station (one with the most records)
    station_activity = (
        session.query(Measurement.station, func.count(Measurement.station))
        .group_by(Measurement.station)
        .order_by(func.count(Measurement.station).desc())
        .first()
    )
    
    most_active_station = station_activity[0]
    
    # Query temperature observations for the last 12 months for this station
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)
    
    tobs_data = (
        session.query(Measurement.tobs)
        .filter(Measurement.station == most_active_station)
        .filter(Measurement.date >= one_year_ago)
        .all()
    )
    
    # Convert the data to a list
    tobs_list = [tobs[0] for tobs in tobs_data]
    
    return jsonify(tobs_list)

# /api/v1.0/<start> - Get temperature stats (min, avg, max) for dates from start to present
@app.route('/api/v1.0/<start>')
def start_date_stats(start):
    # Query the temperature statistics for the start date
    temp_stats = (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs)
        )
        .filter(Measurement.date >= start)
        .all()
    )
    
    # Extract the data from the result
    min_temp, avg_temp, max_temp = temp_stats[0]
    
    # Create a dictionary with the results
    stats = {
        "Start Date": start,
        "TMIN": min_temp,
        "TAVG": avg_temp,
        "TMAX": max_temp
    }
    
    return jsonify(stats)

# /api/v1.0/<start>/<end> - Get temperature stats (min, avg, max) for dates from start to end
@app.route('/api/v1.0/<start>/<end>')
def start_end_date_stats(start, end):
    # Query the temperature statistics for the given date range
    temp_stats = (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs)
        )
        .filter(Measurement.date >= start)
        .filter(Measurement.date <= end)
        .all()
    )
    
    # Extract the data from the result
    min_temp, avg_temp, max_temp = temp_stats[0]
    
    # Create a dictionary with the results
    stats = {
        "Start Date": start,
        "End Date": end,
        "TMIN": min_temp,
        "TAVG": avg_temp,
        "TMAX": max_temp
    }
    
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
