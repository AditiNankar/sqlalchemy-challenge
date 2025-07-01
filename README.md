# 🌦️ SQLAlchemy Challenge — SurfsUp Climate Analysis

## 📘 Overview
This project explores and analyzes climate data for Hawaii using **Python**, **SQLAlchemy**, and data visualization libraries. It reflects database tables into SQLAlchemy ORM, performs exploratory data analysis, and visualizes precipitation and temperature trends.

---

## 📁 Project Structure
sqlalchemy-challenge/
├── SurfsUp/
│   ├── Resources/
│   │   └── hawaii.sqlite          # Climate SQLite database
│   ├── climate_starter.ipynb      # Jupyter notebook for data analysis
│   ├── app.py                     # Flask API app
│   ├── README.md

---

## 🛠️ Tools & Technologies

- Python  
- SQLAlchemy (ORM + Automap)  
- SQLite  
- Flask  
- Pandas  
- Matplotlib  
- Jupyter Notebook  

---

## 🧪 Part 1: Climate Data Exploration

Performed exploratory analysis using the `hawaii.sqlite` database to understand temperature and precipitation trends.

### ✅ Steps Taken

- Connected to SQLite with `SQLAlchemy` using `create_engine()`
- Reflected tables into ORM classes using `automap_base()`
- Created a `Session` and closed it properly after queries

### 🌧️ Precipitation Analysis

- Found the most recent date in dataset: `2017-08-23`
- Queried 12 months of precipitation data using that date
- Loaded into Pandas DataFrame and plotted results
- Summary statistics calculated

📊 **Plot Example:**

![precipitation_plot](Resources/precipitation_plot.png)

---

### 🌡️ Station Analysis

- Found 9 total weather stations
- Identified the most active station: `USC00519281`
- Retrieved min, max, and average temps for that station
- Queried 12 months of TOBS (temperature observations) for it
- Visualized TOBS as a histogram with 12 bins

📊 **Histogram Example:**

![tobs_histogram](Resources/tobs_histogram.png)

---

## 🌐 Part 2: Climate API with Flask

Developed a RESTful API using **Flask** based on prior queries.


## 📤 Deployment & GitHub
	•	Project pushed to GitHub
	•	Proper use of .gitignore to protect sensitive or unnecessary files
	•	Clear, descriptive commit messages used throughout

## 👩‍💻 Author

Aditi Nankar
Aspiring Data Analyst | Python + SQL Enthusiast
