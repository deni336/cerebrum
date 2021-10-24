import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn =  sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return conn

def create_database(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS CAMERAS (ID INT PRIMARY KEY NOT NULL,
    MODEL TEXT NOT NULL,
    SERIAL_NUMBER INT NOT NULL,
    MAC_ADDRESS TEXT NOT NULL,
    IS_AVAILABLE  NOT NULL,
    CHECK_OUT_DATE TEXT NOT NULL,
    CHECK_IN_DATE TEXT NOT NULL,
    CAMERA_LOCATION TEXT NOT NULL,
    WHO_HAS TEXT NOT NULL,
    CAMERA_PASS TEXT NOT NULL,
    PRICE INT NOT NULL);''')
    print("Camera table created successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPUTERS (ID INT PRIMARY KEY NOT NULL,
    PROCESSOR TEXT NOT NULL,
    MODEL TEXT NOT NULL,
    SERVICE_TAG TEXT NOT NULL,
    RAM TEXT NOT NULL,
    PRICE INT NOT NULL);''')
    print("Computer table created successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS JOBS (JOB_NUMBER INT PRIMARY KEY NOT NULL,
    COMPANY TEXT NOT NULL,
    CAMERA_TYPE TEXT NOT NULL,
    CAMERA_COUNT INT NOT NULL,
    CAMERAS TEXT NOT NULL,
    ACCESSORIES TEXT NOT NULL,
    SOFTWARE_MODULES TEXT NOT NULL,
    PURCHASE_DATE TEXT NOT NULL,
    ARRIVAL_DATE TEXT NOT NULL,
    ITEM_APPLICATION TEXT NOT NULL,
    TESTING_STATUS TEXT NOT NULL,
    INFO TEXT);''')
    print("Jobs table created successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS WORKERS (ID INT PRIMARY KEY NOT NULL,
    WORKER_NAME TEXT NOT NULL,
    CAMERAS TEXT NOT NULL,
    ITEMS TEXT NOT NULL);''')
    print("Workers table created successfully")
    conn.commit()
    conn.close()

def create_project(conn, cam):
    sql = "INSERT INTO cameras (ID, MODEL, SERIAL_NUMBER, MAC_ADDRESS, IS_AVAILABLE, CHECK_OUT_DATE, CHECK_IN_DATE, CAMERA_LOCATION, WHO_HAS, CAMERA_PASS, PRICE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, cam)
    conn.commit()
    return cur.lastrowid

def create_task(conn, task):
    sql = "INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"C:\\Projects\\test.db"
    conn =  create_connection(database)
    with conn:
        cam = ('Cool App', '2015-01-01', '2015-01-30')
        id = create_project(conn, cam)

        task_1 = ('Analyze', 1, 1, id, '2015-01-01', '2015-01-30')
        task_2 = ('Confirm', 1, 1, id, '2015-01-01', '2015-01-30')

        create_task(conn, task_1)
        create_task(conn, task_2)

if __name__ == '__main__':
    main()