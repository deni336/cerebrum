import sqlite3
from sqlite3 import Error

database = r"C:\\Projects\\test.db"

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
    conn = create_connection(database)
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

def create_camera(conn, camera):
    conn = create_connection(database)    
    sql = '''INSERT INTO cameras (ID, MODEL, SERIAL_NUMBER, MAC_ADDRESS, IS_AVAILABLE, CHECK_OUT_DATE, CHECK_IN_DATE, CAMERA_LOCATION, WHO_HAS, CAMERA_PASS, PRICE) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, camera)
    conn.commit()
    return cur.lastrowid

def create_job(conn, jobs):
    conn = create_connection(database)
    sql = '''INSERT INTO jobs (JOB_NUMBER, COMPANY, CAMERA_TYPE, CAMERA_COUNT, CAMERAS, ACCESSORIES, SOFTWARE_MODULES, PURCHASE_DATE, ARRIVAL_DATE, ITEM_APPLICATION, TESTING_STATUS, INFO) 
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, jobs)
    conn.commit()
    return cur.lastrowid

def create_worker(conn, worker):
    conn = create_connection(database)
    sql = '''INSERT INTO workers(ID, WORKER_NAME, CAMERAS, ITEMS) 
    VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, worker)
    conn.commit()
    return cur.lastrowid

def create_computer(conn, computer):
    conn = create_connection(database)
    sql = '''INSERT INTO computers(ID, PROCESSORS, MODEL, SERVICE_TAG, RAM, PRICE) 
    VALUES (?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, computer)
    conn.commit()
    return cur.lastrowid

def update_camera(conn, ucamera):
    conn = create_connection(database)
    sql = '''UPDATE cameras
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, ucamera)
    conn.commit()
    return cur.lastrowid

def update_job(conn, ujob):
    conn = create_connection(database)
    sql = '''UPDATE jobs
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, ujob)
    conn.commit()
    return cur.lastrowid

def update_worker(conn, uworker):
    conn = create_connection(database)
    sql = '''UPDATE workers
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, uworker)
    conn.commit()
    return cur.lastrowid

def update_computer(conn, ucomputer):
    conn = create_connection(database)
    sql = '''UPDATE cameras
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, ucomputer)
    conn.commit()
    return cur.lastrowid

def read_camera(conn, rcamera):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM cameras
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, rcamera)
    return cur.lastrowid

def read_job(conn, rjob):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM jobs
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, rjob)
    return cur.lastrowid

def read_worker(conn, rworker):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM workers
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, rworker)
    return cur.lastrowid

def read_computer(conn, rcomputer):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM computers
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, rcomputer)
    return cur.lastrowid

def delete_camera(conn, dcamera):
    conn = create_connection(database)
    sql = '''DELETE FROM cameras
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, dcamera)
    conn.commit()
    return cur.lastrowid

def delete_job(conn, djob):
    conn = create_connection(database)
    sql = '''DELETE FROM jobs
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, djob)
    conn.commit()
    return cur.lastrowid

def delete_worker(conn, dworker):
    conn = create_connection(database)
    sql = '''DELETE FROM workers
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, dworker)
    conn.commit()
    return cur.lastrowid

def delete_computer(conn, dcomputer):
    conn = create_connection(database)
    sql = '''DELETE FROM computers
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, dcomputer)
    conn.commit()
    return cur.lastrowid
    
