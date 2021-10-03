class Worker:
        def _init_(self, id, cameras, items): 
            self.id = id
            self.cameras = [cameras]
            self.items = [items]
        

        def addCamera(self, camera): 
            self.cameras.push(camera)
        
    

