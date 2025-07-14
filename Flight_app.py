import mysql.connector

import pymysql
import pandas as pd
from sqlalchemy import create_engine

# connect to the Data base
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'Dev@$2024',
        database = 'flights_db'
    )
    mycursor = conn.cursor()
    print("Connection established !") 

except :
    print("Connection Error !")



# create a database on the db server
# mycursor.execute("CREATE DATABASE flights_db")
# conn.commit()

df = pd.read_csv('flights_cleaned - flights_cleaned.csv')

engine = create_engine("mysql+pymysql://root:Dev%40%242024@127.0.0.1:3306/flights_db")

df.to_sql('flights', con=engine, if_exists='replace')
