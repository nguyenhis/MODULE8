#1
import mysql.connector
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'dbuser',
    password = 'pass_word'
)
def showairport(icao):
    sql = "select ident, name, iso_country from airport"
    sql += " WHERE ident='" + icao + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The ICAO {row[0]} corresponds to {row[1]} and the country is {row[2]}.")
        return
icao = input("Enter ICAO of the airport to search: ")
showairport(icao)

#2
import mysql.connector
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'dbuser',
    password = 'pass_word')
def list_airports_by_type(country_code):
    # Define the SQL query to retrieve airports in the given country, grouped by type and ordered by type
    sql = """
            SELECT type, COUNT(*) as count
            FROM airport
            WHERE iso_country = %s
            GROUP BY type
            ORDER BY type
        """
    cursor = connection.cursor()
    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[1]} {row[0]} airports")
    else:
            print(f"No airports found for country code: {country_code}")


country_code = input("Enter the country code (e.g., FI for Finland): ")

list_airports_by_type(country_code)



#3

import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='pass_word'
)
def get_airport_coordinates(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        print(f"Airport with ICAO code {icao} not found in the database.")
        return None
def calculate_distance_between_airports(icao1, icao2):
    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)
    if coords1 and coords2:
        # Create geodesic objects using the coordinates
        airport1_coords = (coords1[0], coords1[1])
        airport2_coords = (coords2[0], coords2[1])
        distance = geodesic(airport1_coords, airport2_coords).kilometers
        return distance
    else:
        return None

icao1 = input("Enter ICAO code of the first airport: ")
icao2 = input("Enter ICAO code of the second airport: ")

distance = calculate_distance_between_airports(icao1, icao2)

if distance is not None:
    print(f"The distance between {icao1} and {icao2} is approximately {distance:.2f} kilometers.")
else:
    print("Distance calculation failed. Please check the ICAO codes and ensure they exist in the database.")


connection.close()



