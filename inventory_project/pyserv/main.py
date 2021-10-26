import sqlite3
from sqlite3 import Error

# Testing purposes #
camera = [1, 'A65', 1234567, 'DUMMYMAC123', 'IN', '1/21/21', '1/21/21', 'BIRMINGHAM, AL', 'DENI', 'IEJFY748', 5000]


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
    camera_table = '''CREATE TABLE IF NOT EXISTS CAMERAS (ID INT PRIMARY KEY NOT NULL,
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
    computer_table = '''CREATE TABLE IF NOT EXISTS COMPUTERS (ID INT PRIMARY KEY NOT NULL,
    PROCESSOR TEXT NOT NULL,
    MODEL TEXT NOT NULL,
    SERVICE_TAG TEXT NOT NULL,
    RAM TEXT NOT NULL,
    PRICE INT NOT NULL);'''                
    job_table = '''CREATE TABLE IF NOT EXISTS JOBS (JOB_NUMBER INT PRIMARY KEY NOT NULL,
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
    worker_table = '''CREATE TABLE IF NOT EXISTS WORKERS (ID INT PRIMARY KEY NOT NULL,
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

        
# create_database()

def create_camera(camera):
    conn = create_connection(database)    
    sql = '''INSERT INTO cameras (ID, MODEL, SERIAL_NUMBER, MAC_ADDRESS, IS_AVAILABLE, CHECK_OUT_DATE, CHECK_IN_DATE, CAMERA_LOCATION, WHO_HAS, CAMERA_PASS, PRICE) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, camera)
    conn.commit()
    print("Camera added successfully")
    return cur.lastrowid
create_camera(camera)


def create_job(jobs):
    conn = create_connection(database)
    sql = '''INSERT INTO jobs (JOB_NUMBER, COMPANY, CAMERA_TYPE, CAMERA_COUNT, CAMERAS, ACCESSORIES, SOFTWARE_MODULES, PURCHASE_DATE, ARRIVAL_DATE, ITEM_APPLICATION, TESTING_STATUS, INFO) 
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, jobs)
    conn.commit()
    print("Job added successfully")
    return cur.lastrowid

def create_worker(worker):
    conn = create_connection(database)
    sql = '''INSERT INTO workers(ID, WORKER_NAME, CAMERAS, ITEMS) 
    VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, worker)
    conn.commit()
    print("Worker added successfully")
    return cur.lastrowid

def create_computer(computer):
    conn = create_connection(database)
    sql = '''INSERT INTO computers(ID, PROCESSORS, MODEL, SERVICE_TAG, RAM, PRICE) 
    VALUES (?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, computer)
    conn.commit()
    print("Computer added successfully")
    return cur.lastrowid

def update_camera(ucamera):
    conn = create_connection(database)
    sql = '''UPDATE cameras
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, ucamera)
    conn.commit()
    print("Camera updated successfully")
    return cur.lastrowid

def update_job(ujob):
    conn = create_connection(database)
    sql = '''UPDATE jobs
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, ujob)
    conn.commit()
    print("Job updated successfully")
    return cur.lastrowid

def update_worker(uworker):
    conn = create_connection(database)
    sql = '''UPDATE workers
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, uworker)
    conn.commit()
    print("Worker updated successfully")
    return cur.lastrowid

def update_computer(ucomputer):
    conn = create_connection(database)
    sql = '''UPDATE cameras
    SET (?) = (?)
    WHERE (?) = (?)'''
    cur = conn.cursor()
    cur.execute(sql, ucomputer)
    conn.commit()
    print("Computer updated successfully")
    return cur.lastrowid

def read_camera(rcamera):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM cameras
    WHERE (?) = (?)'''
    cur = conn.cursor()
    read = cur.execute(sql, rcamera)
    return read, cur.lastrowid

def read_job(rjob):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM jobs
    WHERE (?) = (?)'''
    cur = conn.cursor()
    read = cur.execute(sql, rjob)
    return read, cur.lastrowid

def read_worker(rworker):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM workers
    WHERE (?) = (?)'''
    cur = conn.cursor()
    read = cur.execute(sql, rworker)
    return read, cur.lastrowid

def read_computer(rcomputer):
    conn = create_connection(database)
    sql = '''SELECT (?)
    FROM computers
    WHERE (?) = (?)'''
    cur = conn.cursor()
    read = cur.execute(sql, rcomputer)
    return read, cur.lastrowid

def delete_camera(dcamera):
    conn = create_connection(database)
    sql = '''DELETE FROM cameras
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, dcamera)
    conn.commit()
    print("Camera deleted successfully")
    return cur.lastrowid

def delete_job(djob):
    conn = create_connection(database)
    sql = '''DELETE FROM jobs
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, djob)
    conn.commit()
    print("Job deleted successfully")
    return cur.lastrowid

def delete_worker(dworker):
    conn = create_connection(database)
    sql = '''DELETE FROM workers
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, dworker)
    conn.commit()
    print("Worker deleted successfully")
    return cur.lastrowid

def delete_computer(dcomputer):
    conn = create_connection(database)
    sql = '''DELETE FROM computers
    WHERE ID = (?)'''
    cur = conn.cursor()
    cur.execute(sql, dcomputer)
    conn.commit()
    print("Computer deleted successfully")
    return cur.lastrowid
    
def view_table(table):
    conn = create_connection(database)
    sql = '''SELECT *
    FROM (?)'''
    cur = conn.cursor()
    read = cur.execute(sql, table)
    return read, cur.lastrowid
