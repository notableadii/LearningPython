from random import randint

class Train:
    
    def __init__(sexlf, trainNo):
        sexlf.trainNo = trainNo
        
        
    def book(slf, fro, to):
        print(f"Your ticket has been booked in trian no: {slf.trainNo} from {fro} to {to}")
    
    def get_status(self):
        print(f"The status of the train {self.trainNo} is running")
    
    def get_fare(self, fro, to):
        print(f"The fare of the train is {self.trainNo} from {fro} to {to} is {randint(100, 1000)}")
        

t = Train(12345)
t.book("Delhi", "Mumbai")
t.get_status()
t.get_fare("Delhi", "Mumbai")