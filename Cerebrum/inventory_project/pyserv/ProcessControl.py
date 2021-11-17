import sqlite3
import os
from sqlite3 import Error, Cursor


database = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\inventory.db"
databaseBackup = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\inventorybackup.db"


def createConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


class DatabaseCreationProcesses:
    def __init__(self, createDatabase, createBackupDatabase, backupDatabase):
        self.createDatabase = createDatabase
        self.createBackupDatabase = createBackupDatabase
        self.backupDatabase = backupDatabase

    def createDatabase(self):
        conn = createConnection(database)
        cur = conn.cursor()
        cameraTable = '''CREATE TABLE IF NOT EXISTS CAMERA
        (ID INT PRIMARY KEY NOT NULL,
        MODEL TEXT NOT NULL,
        SERIAL_NUMBER TEXT NOT NULL,
        MAC_ADDRESS TEXT NOT NULL,
        IS_AVAILABLE TEXT NOT NULL,
        CHECK_OUT_DATE TEXT NOT NULL,
        CHECK_IN_DATE TEXT NOT NULL,
        CAMERA_LOCATION TEXT NOT NULL,
        WHO_HAS TEXT NOT NULL,
        CAMERA_PASS TEXT NOT NULL,
        PRICE TEXT NOT NULL);'''
        computerTable = '''CREATE TABLE IF NOT EXISTS COMPUTER
        (ID INT PRIMARY KEY NOT NULL,
        PROCESSOR TEXT NOT NULL,
        MODEL TEXT NOT NULL,
        SERVICE_TAG TEXT NOT NULL,
        RAM TEXT NOT NULL,
        PRICE INT NOT NULL);'''
        jobTable = '''CREATE TABLE IF NOT EXISTS JOB
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
        workerTable = '''CREATE TABLE IF NOT EXISTS WORKER
        (ID INT PRIMARY KEY NOT NULL,
        WORKER_NAME TEXT NOT NULL,
        CAMERAS TEXT NOT NULL,
        ITEMS TEXT NOT NULL);'''
        cur.execute(computerTable)
        print("Computer table created successfully")
        cur.execute(jobTable)
        print("Jobs table created successfully")
        cur.execute(workerTable)
        print("Workers table created successfully")
        cur.execute(cameraTable)
        print("Camera table created successfully")
        conn.commit()
        conn.close()

    def createBackupDatabase(self):
        conn = createConnection(databaseBackup)
        cur = conn.cursor()
        cameraTable = '''CREATE TABLE IF NOT EXISTS CAMERA
        (ID INT PRIMARY KEY NOT NULL,
        MODEL TEXT NOT NULL,
        SERIAL_NUMBER TEXT NOT NULL,
        MAC_ADDRESS TEXT NOT NULL,
        IS_AVAILABLE TEXT NOT NULL,
        CHECK_OUT_DATE TEXT NOT NULL,
        CHECK_IN_DATE TEXT NOT NULL,
        CAMERA_LOCATION TEXT NOT NULL,
        WHO_HAS TEXT NOT NULL,
        CAMERA_PASS TEXT NOT NULL,
        PRICE TEXT NOT NULL);'''
        computerTable = '''CREATE TABLE IF NOT EXISTS COMPUTER
        (ID INT PRIMARY KEY NOT NULL,
        PROCESSOR TEXT NOT NULL,
        MODEL TEXT NOT NULL,
        SERVICE_TAG TEXT NOT NULL,
        RAM TEXT NOT NULL,
        PRICE INT NOT NULL);'''
        jobTable = '''CREATE TABLE IF NOT EXISTS JOB
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
        workerTable = '''CREATE TABLE IF NOT EXISTS WORKER
        (ID INT PRIMARY KEY NOT NULL,
        WORKER_NAME TEXT NOT NULL,
        CAMERAS TEXT NOT NULL,
        ITEMS TEXT NOT NULL);'''
        cur.execute(computerTable)
        print("Computer table created successfully")
        cur.execute(jobTable)
        print("Jobs table created successfully")
        cur.execute(workerTable)
        print("Workers table created successfully")
        cur.execute(cameraTable)
        print("Camera table created successfully")
        conn.commit()
        conn.close()

    def backupDatabase(self):
        try:
            conn = createConnection(database)
            conn.backup(createConnection(databaseBackup),
                        pages=0, progress=None)
            conn.commit()
            conn.close()
        except Error as e:
            return e

class ItemCreationProcesses():

    def __init__(self, createCamera, createWorker, createJob, createComputer) -> None:
        self.createCamera = createCamera
        self.createWorker = createWorker
        self.createJob = createJob
        self.createComputer = createComputer

    def createCamera(self, camera):
        conn = createConnection(database)
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

    def createJob(self, job):
        conn = createConnection(database)
        try:
            sql = '''INSERT INTO job (JOB_NUMBER, COMPANY,
                    CAMERA_TYPE, CAMERA_COUNT, CAMERAS, ACCESSORIES,
                    SOFTWARE_MODULES, PURCHASE_DATE, ARRIVAL_DATE,
                    ITEM_APPLICATION, TESTING_STATUS, INFO)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, job)
            conn.commit()
            conn.close()
            print("Job added successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def createWorker(self, worker):
        conn = createConnection(database)
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

    def createComputer(self, computer):
        conn = createConnection(database)
        try:
            sql = '''INSERT INTO computer (ID, PROCESSOR, MODEL,
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

class ItemUpdateProcesses():

    def __init__(self, updateCamera, updateWorker, updateJob, updateComputer) -> None:
        self.updateCamera = updateCamera
        self.updateWorker = updateWorker
        self.updateJob = updateJob
        self.updateComputer = updateComputer

    def updateCamera(self, updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:
            cur = conn.cursor()
            cur.execute('UPDATE CAMERA SET [{0}] = ? WHERE ID = ?'
                        .format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Camera updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def updateJob(self, updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:
            cur = conn.cursor()
            cur.execute('UPDATE Job SET [{0}] = ? WHERE ID = ?'
                        .format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Job updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def updateWorker(self, updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:
            cur = conn.cursor()
            cur.execute('UPDATE WORKER SET [{0}] = ? WHERE ID = ?'
                        .format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Worker updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def updateComputer(self, updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:
            cur = conn.cursor()
            cur.execute('UPDATE COMPUTER SET [{0}] = ? WHERE ID = ?'
                        .format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Computer updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

class ItemReadProcesses():

    def __init__(self, readCamera, readWorker, readJob, readComputer) -> None:
        self.readCamera = readCamera
        self.readWorker = readWorker
        self.readJob = readJob
        self.readComputer = readComputer

    def readCamera(self, searchColumn, searchValue):
        conn = createConnection(database)
        read = []
        try:
            sql = 'SELECT * FROM CAMERA WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)
            conn.close()
        except Error as e:
            print(e)
        return read

    def readJob(self, searchColumn, searchValue):
        conn = createConnection(database)
        read = []
        try:
            sql = 'SELECT * FROM JOB WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)
            conn.close()
        except Error as e:
            print(e)
        return read

    def readWorker(self, searchColumn, searchValue):
        conn = createConnection(database)
        read = []
        try:
            sql = 'SELECT * FROM Worker WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)
            conn.close()
        except Error as e:
            print(e)
        return read

    def readComputer(self, searchColumn, searchValue):
        conn = createConnection(database)
        read = []
        try:
            sql = 'SELECT * FROM COMPUTER WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)
            conn.close()
        except Error as e:
            print(e)
        return read

class ItemDeleteProcesses():

    def __init__(self, deleteCamera, deleteWorker, deleteJob, deleteComputer) -> None:
        self.deleteCamera = deleteCamera
        self.deleteWorker = deleteWorker
        self.deleteJob = deleteJob
        self.deleteComputer = deleteComputer

    def deleteCamera(self, dcamera):
        conn = createConnection(database)
        try:
            sql = '''DELETE FROM CAMERA
                    WHERE ID = ?'''
            cur = conn.cursor()
            cur.execute(sql, (dcamera))
            conn.commit()
            conn.close()
            print("Camera deleted successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def deleteJob(self, djob):
        conn = createConnection(database)
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

    def deleteWorker(self, dworker):
        conn = createConnection(database)
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

    def deleteComputer(self, dcomputer):
        conn = createConnection(database)
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
    
class ItemViewProcesses():

    def __init__(self, viewCameraTable, viewWorkerTable, viewJobTable, viewComputerTable,
                 viewReadme) -> None:
        self.viewCameraTable = viewCameraTable
        self.viewWorkerTable = viewWorkerTable
        self.viewJobTable = viewJobTable
        self.viewComputerTable = viewComputerTable
        self.viewReadme = viewReadme

    def viewCameraTable(self):
        conn = createConnection(database)
        sql = '''SELECT *
                FROM camera '''
        cur = conn.cursor()
        cameraTable = []
        for row in cur.execute(sql):
            cameraTable.append(row)
        conn.close()
        return cameraTable

    def viewWorkerTable(self):
        conn = createConnection(database)
        sql = '''SELECT *
                FROM worker '''
        cur = conn.cursor()
        workerTable = []
        for row in cur.execute(sql):
            workerTable.append(row)
        conn.close()
        return workerTable

    def viewComputerTable(self):
        conn = createConnection(database)
        sql = '''SELECT *
                FROM computer '''
        cur = conn.cursor()
        computerTable = []
        for row in cur.execute(sql):
            computerTable.append(row)
        conn.close()
        return computerTable

    def viewJobTable(self):
        conn = createConnection(database)
        sql = '''SELECT *
                FROM job '''
        cur = conn.cursor()
        jobTable = []
        for row in cur.execute(sql):
            jobTable.append(row)
        conn.close()
        return jobTable

    def viewReadme(self):
        os.system('''start "+"C:\\Projects\\python_projects\\
                    cerebrum\\Cerebrum\\readme.md''')
