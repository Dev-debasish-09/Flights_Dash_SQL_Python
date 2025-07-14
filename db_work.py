import mysql.connector

class DB:
    def __init__(self):
        #connect to data base 
        try:
            self.conn = mysql.connector.connect(
                host = '127.0.0.1',
                user = 'root',
                password = 'Dev@$2024',
                database = 'flights_db'
            )
            self.mycursor = self.conn.cursor()
            print("Connection established !") 

        except :
            print("Connection Error !")

    def fetch_city_names(self):

        city = []

        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM flights_db.flights
        UNION
        SELECT DISTINCT(Source) FROM flights_db.flights;
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
        return city
    def featch_all_flights(self,source,destination):
        self.mycursor.execute("""
                            SELECT Airline,Route,Dep_time,Duration,Price FROM flights_db.flights
                            WHERE Source = '{}' AND Destination = '{}'""".format(source,destination))
        data = self.mycursor.fetchall()
        return data
    
    def fetch_airline_frequency(self):

        Airline = []
        frequency = []

        self.mycursor.execute("""
                            SELECT Airline,COUNT(*) FROM flights_db.flights
                            GROUP BY Airline;
                            """)
        data = self.mycursor.fetchall()

        for item in data:
            Airline.append(item[0])
            frequency.append(item[1])
        return Airline,frequency
    
    def busy_airport(self):

        city = []
        frequency = []

        self.mycursor.execute("""
                            SELECT Source,COUNT(*) FROM (SELECT Source FROM flights_db.flights
							UNION ALL
                            SELECT Destination FROM flights_db.flights) t
                            GROUP BY t.Source
                            ORDER BY COUNT(*) DESC;""")
        
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city,frequency
    
    def daily_frequency(self):
        date = []
        frequency = []

        self.mycursor.execute("""
                            SELECT Date_of_Journey,COUNT(*) FROM flights_db.flights
                            GROUP BY Date_of_Journey""")
        
        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date,frequency

        

