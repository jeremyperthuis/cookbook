import sqlite3



def create_connection(db):
    conn = None
    try :
        conn = sqlite3.connect(db)
        print(sqlite3.version)
        return conn

    except sqlite3.Error as e:
        print(e)

    return conn

def create_table_employee(conn):
    request = ''' CREATE TABLE IF NOT EXISTS employee(
                        name text,
                        age integer,
                        start_date text
                        );'''
    try:
        c = conn.cursor()
        c.execute(request)
    except sqlite3.Error as e:
        print("ERROR create table : {}".format(e))

def add_employee(conn, data):
    try :
        c = conn.cursor()
        c.executemany('INSERT INTO employee VALUES(?,?,?)', data)
        conn.commit()
    except sqlite3.Error as e:
        print("ERROR ad employee : {}".format(e))


def get_all_employees(conn):
    try:
        c = conn.cursor()
        c.execute('SELECT * FROM employee;')
        rows = c.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("ERROR get employees : {}".format(e))



data = [('jean', 34, "2020-04-23"),
        ('Marie', 23, "2019-12-04"),
        ('Frank', 57, "1998-01-17")]


conn = create_connection("db/test_data.db")
if conn is not None:
    create_table_employee(conn)
    #add_employee(conn, data)
    get_all_employees(conn)
    conn.close()



