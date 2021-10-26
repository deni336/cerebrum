import sqlite3
from sqlite3 import Error

# Testing purposes #
camera1 = [1, 'A65', 1234567, 'DUMMYMAC123', 'IN', '1/21/21', '1/21/21', 'BIRMINGHAM, AL', 'DENI', 'IEJFY748', 5000]
camera2 = [2, 'A700', 7654321, 'DUMMYMAC123', 'IN', '1/21/21', '1/21/21', 'BIRMINGHAM, AL', 'DENI', 'IEJFY748', 5000]
camera3 = [3, 'A400', 5475632, 'DUMMYMAC123', 'IN', '1/21/21', '1/21/21', 'BIRMINGHAM, AL', 'DENI', 'IEJFY748', 5000]
camera4 = [4, 'A50', 3375622, 'DUMMYMAC123', 'IN', '1/21/21', '1/21/21', 'BIRMINGHAM, AL', 'DENI', 'IEJFY748', 5000]


# Testing purposes #


database = r"C:\\Projects\\python_projects\\cerebrum\\inventory_project\\test.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)    

def create_database():
    conn = create_connection(database)    
    cur = conn.cursor()
    camera_table = '''CREATE TABLE IF NOT EXISTS CAMERA
    (ID INT PRIMARY KEY NOT NULL,
    MODEL TEXT NOT NULL,
    SERIAL_NUMBER INT NOT NULL,
    MAC_ADDRESS TEXT NOT NULL,
    IS_AVAILABLE  NOT NULL,
    CHECK_OUT_DATE TEXT NOT NULL,
    CHECK_IN_DATE TEXT NOT NULL,
    CAMERA_LOCATION TEXT NOT NULL,
    WHO_HAS TEXT NOT NULL,
    CAMERA_PASS TEXT NOT NULL,
    PRICE INT NOT NULL);'''        
    computer_table = '''CREATE TABLE IF NOT EXISTS COMPUTER
    (ID INT PRIMARY KEY NOT NULL,
    PROCESSOR TEXT NOT NULL,
    MODEL TEXT NOT NULL,
    SERVICE_TAG TEXT NOT NULL,
    RAM TEXT NOT NULL,
    PRICE INT NOT NULL);'''                
    job_table = '''CREATE TABLE IF NOT EXISTS JOB
    (JOB_NUMBER INT PRIMARY KEY NOT NULL,
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
    INFO TEXT);'''        
    worker_table = '''CREATE TABLE IF NOT EXISTS WORKER
    (ID INT PRIMARY KEY NOT NULL,
    WORKER_NAME TEXT NOT NULL,
    CAMERAS TEXT NOT NULL,
    ITEMS TEXT NOT NULL);'''        
    cur.execute(computer_table)
    print("Computer table created successfully")
    cur.execute(job_table)
    print("Jobs table created successfully")
    cur.execute(worker_table)
    print("Workers table created successfully")
    cur.execute(camera_table)
    print("Camera table created successfully")
    conn.commit()
    conn.close()

create_database()

def create_camera(camera):
    conn = create_connection(database)
    try:
        sql = '''INSERT INTO camera (ID, MODEL,
                 SERIAL_NUMBER, MAC_ADDRESS, IS_AVAILABLE,
                 CHECK_OUT_DATE, CHECK_IN_DATE, CAMERA_LOCATION,
                 WHO_HAS, CAMERA_PASS, PRICE) 
                 VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, camera)
        conn.commit()
        conn.close()
        print("Camera added successfully")
    except Error as e:
        print(e)
    return cur.lastrowid
create_camera(camera1)
create_camera(camera2)
create_camera(camera3)
create_camera(camera4)


def create_job(jobs):
    conn = create_connection(database)
    try:
        sql = '''INSERT INTO job (JOB_NUMBER, COMPANY,
                 CAMERA_TYPE, CAMERA_COUNT, CAMERAS, ACCESSORIES,
                 SOFTWARE_MODULES, PURCHASE_DATE, ARRIVAL_DATE,
                 ITEM_APPLICATION, TESTING_STATUS, INFO) 
                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, jobs)
        conn.commit()
        conn.close()
        print("Job added successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def create_worker(worker):
    conn = create_connection(database)
    try:
        sql = '''INSERT INTO worker (ID, WORKER_NAME, CAMERAS, ITEMS) 
                 VALUES (?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, worker)
        conn.commit()
        conn.close()
        print("Worker added successfully")
    except Error as e:
        print(e)    
    return cur.lastrowid

def create_computer(computer):
    conn = create_connection(database)
    try:
        sql = '''INSERT INTO computer (ID, PROCESSORS, MODEL,
                 SERVICE_TAG, RAM, PRICE) 
                 VALUES (?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, computer)
        conn.commit()
        conn.close()
        print("Computer added successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def update_camera(ucamera):
    conn = create_connection(database)
    try:
        sql = '''UPDATE camera
                 SET (?) = (?)
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        cur.execute(sql, ucamera)
        conn.commit()
        conn.close()
        print("Camera updated successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def update_job(ujob):
    conn = create_connection(database)
    try:
        sql = '''UPDATE job
                 SET (?) = (?)
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        cur.execute(sql, ujob)
        conn.commit()
        conn.close()
        print("Job updated successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def update_worker(uworker):
    conn = create_connection(database)
    try:
        sql = '''UPDATE worker
                 SET (?) = (?)
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        cur.execute(sql, uworker)
        conn.commit()
        conn.close()
        print("Worker updated successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def update_computer(ucomputer):
    conn = create_connection(database)
    try:
        sql = '''UPDATE camera
                 SET (?) = (?)
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        cur.execute(sql, ucomputer)
        conn.commit()
        conn.close()
        print("Computer updated successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def read_camera(rcamera):
    conn = create_connection(database)
    try:
        sql = '''SELECT (?)
                 FROM camera
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        read = cur.execute(sql, rcamera)
        conn.close()
    except Error as e:
        print(e)
    return read, cur.lastrowid

def read_job(rjob):
    conn = create_connection(database)
    try:
        sql = '''SELECT (?)
                 FROM job
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        read = cur.execute(sql, rjob)
        conn.close()
    except Error as e:
        print(e)
    return read, cur.lastrowid

def read_worker(rworker):
    conn = create_connection(database)
    try:
        sql = '''SELECT (?)
                 FROM worker
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        read = cur.execute(sql, rworker)
        conn.close()
    except Error as e:
        print(e)
    return read, cur.lastrowid

def read_computer(rcomputer):
    conn = create_connection(database)
    try:
        sql = '''SELECT (?)
                 FROM computer
                 WHERE (?) = (?)'''
        cur = conn.cursor()
        read = cur.execute(sql, rcomputer)
        conn.close()
    except Error as e:
        print(e)
    return read, cur.lastrowid

def delete_camera(dcamera):
    conn = create_connection(database)
    try:
        sql = '''DELETE FROM camera
                 WHERE ID = (?)'''
        cur = conn.cursor()
        cur.execute(sql, dcamera)
        conn.commit()
        conn.close()
        print("Camera deleted successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def delete_job(djob):
    conn = create_connection(database)
    try:
        sql = '''DELETE FROM job
                 WHERE ID = (?)'''
        cur = conn.cursor()
        cur.execute(sql, djob)
        conn.commit()
        conn.close()
        print("Job deleted successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def delete_worker(dworker):
    conn = create_connection(database)
    try:
        sql = '''DELETE FROM worker
                 WHERE ID = (?)'''
        cur = conn.cursor()
        cur.execute(sql, dworker)
        conn.commit()
        conn.close()
        print("Worker deleted successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

def delete_computer(dcomputer):
    conn = create_connection(database)
    try:
        sql = '''DELETE FROM computer
                 WHERE ID = (?)'''
        cur = conn.cursor()
        cur.execute(sql, dcomputer)
        conn.commit()
        conn.close()
        print("Computer deleted successfully")
    except Error as e:
        print(e)
    return cur.lastrowid

table = ['camera', 'A65']

def view_table():
    conn = create_connection(database)
    sql = '''SELECT *
             FROM camera '''
    cur = conn.cursor()
    for row in cur.execute(sql):
        print(row)
    conn.close()
    return cur.lastrowid
view_table()