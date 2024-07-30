import sqlite3
from sqlite3 import Error

def create_connection(df_file):
    """create a database connection to the Sqlite database
        specified by df_file
    :param db_file: database file
    :return: Connection object or None
    """
    
    conn = None
    try:
        conn = sqlite3.connect(df_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    """craete a table from create_table_sql statement
    :param conn: Connection object
    : param create_table_sql: a CREATE TABLE statement
    :return:
    """
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"/home/pi/Documents/Watering system/gardening.db"
    
    sql_create_waterpump_table = """CREATE TABLE IF NOT EXISTS waterpump (
                                date timestamp DEFAULT CURRENT_TIMESTAMP,
                                pin integer,
                                seconds integer
                                );"""
    # create a db connection
    conn = create_connection(database)
    
    # create tables
    if conn is not None:
        
        # create waterpump table
        create_table(conn, sql_create_waterpump_table)
                
if __name__ == '__main__':
    main()

