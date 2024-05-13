import json
import sqlite3
import mysql.connector

# Fonction pour créer une table SQLite
def create_sqlite_table():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    last_updated_epoch INTEGER,
                    last_updated TEXT,
                    temp_c REAL,
                    temp_f REAL,
                    is_day INTEGER,
                    condition_text TEXT,
                    condition_icon TEXT,
                    condition_code INTEGER,
                    wind_mph REAL,
                    wind_kph REAL,
                    wind_degree INTEGER,
                    wind_dir TEXT,
                    pressure_mb REAL,
                    pressure_in REAL,
                    precip_mm REAL,
                    precip_in REAL,
                    humidity INTEGER,
                    cloud INTEGER,
                    feelslike_c REAL,
                    feelslike_f REAL,
                    vis_km REAL,
                    vis_miles REAL,
                    uv REAL,
                    gust_mph REAL,
                    gust_kph REAL
                    )''')
    conn.commit()
    conn.close()

# Fonction pour insérer des données dans SQLite
def insert_into_sqlite(data):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (data['last_updated_epoch'], data['last_updated'], data['temp_c'], data['temp_f'], data['is_day'],
               data['condition']['text'], data['condition']['icon'], data['condition']['code'],
               data['wind_mph'], data['wind_kph'], data['wind_degree'], data['wind_dir'],
               data['pressure_mb'], data['pressure_in'], data['precip_mm'], data['precip_in'],
               data['humidity'], data['cloud'], data['feelslike_c'], data['feelslike_f'],
               data['vis_km'], data['vis_miles'], data['uv'],
               data['gust_mph'], data['gust_kph']))
    conn.commit()
    conn.close()

# Fonction pour créer une table MySQL
def create_mysql_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="weather_data"
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                    last_updated_epoch INT,
                    last_updated VARCHAR(255),
                    temp_c FLOAT,
                    temp_f FLOAT,
                    is_day INT,
                    condition_text TEXT,
                    condition_icon TEXT,
                    condition_code INT,
                    wind_mph FLOAT,
                    wind_kph FLOAT,
                    wind_degree INT,
                    wind_dir VARCHAR(255),
                    pressure_mb FLOAT,
                    pressure_in FLOAT,
                    precip_mm FLOAT,
                    precip_in FLOAT,
                    humidity INT,
                    cloud INT,
                    feelslike_c FLOAT,
                    feelslike_f FLOAT,
                    vis_km FLOAT,
                    vis_miles FLOAT,
                    uv FLOAT,
                    gust_mph FLOAT,
                    gust_kph FLOAT
                    )''')
    conn.commit()
    conn.close()

# Fonction pour insérer des données dans MySQL
def insert_into_mysql(data):
    conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="weather_data"
    )
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                   (data['last_updated_epoch'], data['last_updated'], data['temp_c'], data['temp_f'], data['is_day'],
                    data['condition']['text'], data['condition']['icon'], data['condition']['code'],
                    data['wind_mph'], data['wind_kph'], data['wind_degree'], data['wind_dir'],
                    data['pressure_mb'], data['pressure_in'], data['precip_mm'], data['precip_in'],
                    data['humidity'], data['cloud'], data['feelslike_c'], data['feelslike_f'],
                    data['vis_km'], data['vis_miles'], data['uv'],
                    data['gust_mph'], data['gust_kph']))
    conn.commit()
    conn.close()

# Exemple de données JSON
weather_data_json = '''
{
    "last_updated_epoch": 1673620200,
    "last_updated": "2023-01-13 14:30",
    "temp_c": 8.7,
    "temp_f": 47.7,
    "is_day": 1,
    "condition": {
        "text": "Partly cloudy",
        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
        "code": 1003
    },
    "wind_mph": 24.2,
    "wind_kph": 38.9,
    "wind_degree": 260,
    "wind_dir": "W",
    "pressure_mb": 1005.0,
    "pressure_in": 29.68,
    "precip_mm": 0.0,
    "precip_in": 0.0,
    "humidity": 74,
    "cloud": 75,
    "feelslike_c": 4.4,
    "feelslike_f": 39.9,
    "vis_km": 10.0,
    "vis_miles": 6.0,
    "uv": 2.0,
    "gust_mph": 33.1,
    "gust_kph": 53.3
}
'''

# Charger les données JSON
weather_data = json.loads(weather_data_json)

# Créer les tables (si besoin)
#create_sqlite_table()
#create_mysql_table()

# Insérer les données
insert_into_sqlite(weather_data)
insert_into_mysql(weather_data)
