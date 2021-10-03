

class Camera:
        def _init_(self, id, model, serial, status, checkoutDate, checkinDate, location, who_has, password): 
            self.id = id
            self.model = model
            self.serial = serial
            self.status = status
            self.checkoutDate = checkoutDate
            self.checkinDate = checkinDate
            self.location = location
            self.who_has = who_has
            self.password = password
        

        def checkOut(self, who_has, location): 
            self.status = "OUT"
            self.who_has = who_has
            self.location = location
        

        def checkIn(self, model, serial): 
            self.model = model
            self.serial = serial
            self.status = "IN"
        
    