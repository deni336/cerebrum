import sqlite3
from sqlite3.dbapi2 import Cursor

#Creates the database and adds the four required tables.
def create_database():
    conn = sqlite3.connect("test.db")
    print("Connected to Database")
    conn.execute('''CREATE TABLE IF NOT EXISTS CAMERAS (ID INT PRIMARY KEY NOT NULL, MODEL TEXT NOT NULL, SERIAL_NUMBER INT NOT NULL, MAC_ADDRESS TEXT NOT NULL, IS_AVAILABLE  NOT NULL, CHECK_OUT_DATE TEXT NOT NULL, CHECK_IN_DATE TEXT NOT NULL, CAMERA_LOCATION TEXT NOT NULL, WHO_HAS TEXT NOT NULL, CAMERA_PASS TEXT NOT NULL, PRICE INT NOT NULL);''')
    print("Camera table created successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPUTERS (ID INT PRIMARY KEY NOT NULL, PROCESSOR TEXT NOT NULL , MODEL TEXT NOT NULL, SERVICE_TAG TEXT NOT NULL, RAM TEXT NOT NULL, PRICE INT NOT NULL);''')
    print("Computer table created successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS JOBS (JOB_NUMBER INT PRIMARY KEY NOT NULL, COMPANY TEXT NOT NULL, CAMERA_TYPE TEXT NOT NULL, CAMERA_COUNT INT NOT NULL, CAMERAS TEXT NOT NULL, ACCESSORIES TEXT NOT NULL, SOFTWARE_MODULES TEXT NOT NULL, PURCHASE_DATE TEXT NOT NULL, ARRIVAL_DATE TEXT NOT NULL, ITEM_APPLICATION TEXT NOT NULL, TESTING_STATUS TEXT NOT NULL, INFO TEXT);''')
    print("Jobs table created successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS WORKERS (ID INT PRIMARY KEY NOT NULL, WORKER_NAME TEXT NOT NULL, CAMERAS TEXT NOT NULL, ITEMS TEXT NOT NULL);''')
    print("Workers table created successfully")
    conn.commit()
    conn.close()
create_database()

#This will be the front end input for a new camera.
cam = [1, 'A65', 1234567, 'DUMMYMAC123', 'IN', '1/21/21', '1/21/21', 'BIRMINGHAM, AL', 'DENI', 'IEJFY748', 5000]

def add_camera(id, model, serial_number, mac_address, is_available, check_out_date, check_in_date, camera_location, who_has, camera_pass, price):
    try:
        conn = sqlite3.connect("test.db")
        cur = conn.cursor()
        print("Connected to Database")
        sqlite3_insert_with_param = "INSERT INTO CAMERAS (ID, MODEL, SERIAL_NUMBER, MAC_ADDRESS, IS_AVAILABLE, CHECK_OUT_DATE, CHECK_IN_DATE, CAMERA_LOCATION, WHO_HAS, CAMERA_PASS, PRICE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cam_tuple = (id, model, serial_number, mac_address, is_available, check_out_date, check_in_date, camera_location, who_has, camera_pass , price)
        cur.execute(sqlite3_insert_with_param, cam_tuple)
        conn.commit()
        print("Camera added to Database")
        cur.close()

    except sqlite3.Error as error:
        print("Failed to add camera to Database")
    finally: 
        if sqlite3.connect:
            conn.close()
            print("Connection to Database closed")
        
add_camera(cam[0], cam[1], cam[2], cam[3], cam[4], cam[5], cam[6], cam[7], cam[8], cam[9], cam[10])

#Will display all cameras from the database. 
def view_cameras_database():
    conn = sqlite3.connect('test.db')
    print('Connected to Database')
    cur = conn.execute("SELECT id, model, serial_number, mac_address, is_available, check_out_date, check_in_date, camera_location, who_has, camera_pass, price FROM CAMERAS")
    for row in cur:
        print("id = ", row[0], "model = ", row[1], "serial_number = ", row[2], "mac_address = ", row[3], "is_available =", row[4], "checkoutDate = ", row[5], "checkinDate = ", row[6], "camera_location = ", row[7], "who_has = ", row[8], "camera_pass = ", row[9], "price = ", row[10])
    print("End of Data")
    conn.close()
view_cameras_database()