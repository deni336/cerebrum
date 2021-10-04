import json
from os import name

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

class Worker:
        def __init__(self, id, cameras, items): 
            self.id = id
            self.cameras = [cameras]
            self.items = [items]
        

        def addCamera(self, camera): 
            self.cameras.push(camera)

class Jobs:
    def __init__(self,PO, job_number, company, camera_type, camera_count, cameras, accessories, software_modules, purchase_date, arrival_date, application, testing_status, info):
        self.PO = PO
        self.job_number = job_number
        self.company = company
        self.camera_type = camera_type
        self.camera_count = camera_count
        self.cameras = cameras
        self.accessories = accessories
        self.software_modules = software_modules
        self.purchase_date = purchase_date
        self.arrival_date = arrival_date
        self.application = application
        self.testing_status = testing_status
        self.info = info

class Computer:
    def __init__(self, processor, model, ram, service_tag, nic_capability, price):
        self.processor = processor
        self.model = model
        self.ram = ram
        self.service_tag = service_tag
        self.nic_capability = nic_capability
        self.price = price

f = ("C:\\Projects\\cerebrum\\cerebrum\\inventory_project\\pyserv\\test.json")

#***************************Cameras*************************

def display_data():
    with open(f) as f1:
        data = json.load(f1)
        print(data)
        return data

def read_from_database(search):
    with open(f) as f1:
        data = json.load(f1)
        return data[search] 

def write_to_database(data):
    with open(f, "w") as fw1:
        json.dump(data, fw1, indent = 2)
    # Add in backup for DB ****************************************************************
    # with open(f, "w") as fw1:
    #     json.dump(data, fw1, indent = 2)
        
    return print("Success!")

cam = Camera(3, "A65", 1213421212, "dummy234", "01/01/2021", "02/02/2021", "Birmingham, AL", "IN", "Mundo", "XxXxXx", 5000)

def add_camera_to_inventory(camera):
    with open(f) as f1:
        data = json.load(f1)
        item = data["cameras"]
        if camera.__dict__ in item:
            return 
        item.append(camera.__dict__)
        return write_to_database(data)

def get_camera_from_inventory(mval, serial):    
    for i in read_from_database("cameras"):
        if serial is not type(int):
            return 
        if i.get("model") == mval and i.get("serial") == serial:
            return i       


def update_camera_info(model_value, serial, key, val):
    with open(f) as f1:
        data = json.load(f1)
        item = data["cameras"]
        for i in item:
            if serial is not type(int):
                return
            if i.get("model") == model_value and i.get("serial") == serial:
                i[key] = val
            return write_to_database(data)
        
#**********************Computers**********************

comp = Computer("i5", "Inspiron 7373", "8gb", "3IDCY44", "ethernet", 1200)
def add_computer_to_inventory(computer):
    with open(f) as f1:
        data = json.load(f1)        
        item = data["computers"]
        if computer.__dict__ in item:
            return 
        item.append(computer.__dict__)
        return write_to_database(data)

def get_computer_from_inventory(mval, service_tag):    
    for i in read_from_database("computers"):
        if i.get("model") == mval and i.get("service_tag") == service_tag:
            print(i)
            return i

def update_computer_info(model_value, service_tag, key, val):
    with open(f) as f1:
        data = json.load(f1)
        item = data["computers"]
        for i in item:
            if i.get("model") == model_value and i.get("service_tag") == service_tag:
                i[key] = val
            return write_to_database(data)

#*************************Workers***********************

def add_worker_to_database(worker):
    with open(f) as f1:
        data = json.load(f1)
        item = data["worker"]
        if worker.__dict__ in item:
            return 
        item.append(worker.__dict__)
        return write_to_database(data)

def get_worker_from_database(name):    
    for i in read_from_database("worker"):
        if i.get("name") == name:
            print(i)        
            return i

def update_worker_info(name, key, check_item, val):
    with open(f) as f1:
        data = json.load(f1)
        item = data["workers"]
        check = data[key]
        for i in item:
            if i.get("name") == name:
                if val is Camera():
                    print(val.__dict__)
                #     if check_item:
                #         val.who_has = name
                #         val.checkOut(val.who_has, val.location)
                #         return i.addCamera(val)
                    
            # return write_to_database(data)
update_worker_info("jacob", "cameras", True, cam)

#*************************Jobs*************************

def add_jobs_to_database(jobs):
    with open(f) as f1:
        data = json.load(f1)
        item = data["jobs"]
        if jobs.__dict__ in item:
            return 
        item.append(jobs.__dict__)
        return write_to_database(data)

def get_jobs_from_database(job_number):    
    for i in read_from_database("jobs"):
        if i.get("job_number") == job_number:
            print(i)
            return i

def update_jobs_info(job_number, key, val):
    with open(f) as f1:
        data = json.load(f1)
        item = data["jobs"]
        for i in item:
            if i.get("job_number") == job_number:
                i[key] = val
            return write_to_database(data)