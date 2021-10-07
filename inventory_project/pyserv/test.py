import json
from os import name
import sqlite3



class Camera:
        def __init__(self, id, model, serial, mac_address, status, checkoutDate, checkinDate, location, who_has, password, price, ): 
            self.id = id
            self.model = model
            self.serial = serial
            self.mac_address = mac_address
            self.status = status
            self.checkoutDate = checkoutDate
            self.checkinDate = checkinDate
            self.location = location
            self.who_has = who_has
            self.password = password
            self.price = price
        

        def checkOut(self, who_has, location): 
            self.status = "OUT"
            self.who_has = who_has
            self.location = location
        

        def checkIn(self, model, serial): 
            self.model = model
            self.serial = serial
            self.status = "IN"

cam = Camera(3, "A65", 1213421212, "dummy234", "01/01/2021", "02/02/2021", "Birmingham, AL", "IN", "Mundo", "XxXxXx", 5000)

def add_camera_to_inventory(c):
    try:
        cur.execute("INSERT INTO Cameras(id, model, serial, mac, lastcheckoutdate, lastcheckindate, location, status, whohas, password, price) VALUES (cam.id, cam.model, cam.serial, cam.mac_address, cam.checkoutDate, cam.checkinDate, cam.location, cam.status, cam.who_has, cam.password, cam.price)")
        row = cur.fetchone()
        # print(id, "=>", row[0], type(row[0]))
    except Exception as ex:
        print(ex)

# add_camera_to_inventory(cam)
sqlite3.register_adapter(Camera, add_camera_to_inventory)
sqlite3.register_converter("camera", add_camera_to_inventory)

con = sqlite3.connect("C:\\Projects\\cerebrum\\cerebrum\\inventory_project\\data\\inventory.db")
cur = con.cursor()
cur.execute("insert into cameras(id, model, serial, mac, lastcheckoutdate, lastcheckindate, location, status, whohas, password, price) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (1, cam.model, cam.serial, cam.mac_address, cam.checkoutDate, cam.checkinDate, cam.location, cam.status, cam.who_has, cam.password, cam.price))
# cur.execute('select p as "p [point]" from test')
# print("with column names:", cur.fetchone()[0])
cur.close()
con.close()

