import json

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

class jobs:
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

class computer:
    def __init__(self, processor, model, ram, serial_number, nic_capability, price):
        self.processor = processor
        self.model = model
        self.ram = ram
        self.serial_number = serial_number
        self.nic_capability = nic_capability
        self.price = price
        

def read_from_database(search):
    with open("C:\\Projects\\cerebrum\\cerebrum\\inventory_project\\pyserv\\test.json") as f:
        data = json.load(f)
        k = data.keys()
        #print(data[search])
        return data[search]

def write_to_database(data):
    with open("C:\\Projects\\cerebrum\\cerebrum\\inventory_project\\pyserv\\test.json", "w") as f:
            json.dump(data, f, indent = 2)
            print(data)
    return print("Success!")


        
            
        
        # if first_search in k:
        #     v = data[first_search]
        #     for i in v:
        #         if sec_search == "serial" or sec_search == "price":
        #             values_search = int(values_search)
        #             #return print(i)                   
        #         elif sec_search in i and i[sec_search] == values_search:
        #             return print(i)
                               
        # else:
        #     print("No Valid Key")
        
        # print(k, v)
#read_from_database(input())


cam = Camera(3, "A65", 1213421212, "dummy234", "01/01/2021", "02/02/2021", "Birmingham, AL", "IN", "Mundo", "XxXxXx", 5000)
# print(cam)
# cam.id = 4
# cam.model = "A35"
# def add_camera_to_inventory(camera):
#         item = read_from_database("cameras")
#         item.append(camera.__dict__)
        
        # print(item)            
        
    
#add_camera_to_inventory(cam)


def get_camera_from_inventory(mval, serial):    
        for i in read_from_database("cameras"):
            if i.get("model") == mval and i.get("serial") == serial:
                print(i)
                return i
                
        
        
get_camera_from_inventory(input(), int(input()))
d2 = []
def update_camera_info(model_value, serial, key, val):
    with open("C:\\Projects\\cerebrum\\cerebrum\\inventory_project\\pyserv\\test.json") as f:
        data = json.load(f)
        item = data["cameras"]
        for i in item:
            if i.get("model") == model_value and i.get("serial") == serial:
                i[key] = val
                d2.append(data)
        with open("C:\\Projects\\cerebrum\\cerebrum\\inventory_project\\pyserv\\test.json", "w") as f:
            json.dump(data, f, indent = 2)
        
            
        
# update_camera_info("A65", 1212121212, "serial", 17777777)

# print(d2)

