
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database conenction to the SQlite database
        specified by db_file
    :param db_file: database file
    :return: connection object or None
    """
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def create_watered(conn, watering):
    """
    Create a new watering event into the waterpump table
    :param conn:
    :param watering:
    """
    
    sql = ''' INSERT INTO waterpump(pin, seconds)
              VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, watering)
    conn.commit()


def write_watering(pin, seconds):
    database = r"/home/pi/Documents/Watering system/gardening.db"
    
    # create a db connection
    conn = create_connection(database)
    
    with conn:
        #create a new game
        watering = (pin, seconds)
        
        create_watered(conn, watering)
        
