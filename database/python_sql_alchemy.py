from sqlalchemy import create_engine
import os

cwd = os.getcwd()

db_uri = 'sqlite:///' + cwd + '/cities.db'
engine = create_engine(db_uri)

def get_cities_by_latitude(latitude):
    n_hemisphere = str(latitude) + '%'
    s_hemisphere = '-' + str(latitude) + '%'
    result = engine.execute("SELECT country, city, region, latitude, longitude "
                            "FROM city "
                            "WHERE (latitude LIKE '" + n_hemisphere + "' "
                            "OR latitude LIKE '" + s_hemisphere + "');")
    data = result.fetchall()
    return data