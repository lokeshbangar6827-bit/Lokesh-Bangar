from Vehicle import vehicle

class Bike(vehicle):
    def __init__(self,fuel_type,brand,color,price):
        self.color=color
        self.price=price
        super().__init__(fuel_type,brand) #super :- parent calling
        
    def ride(self):
        return "bike ride so fast !"
    
    
    def custom_start(self):
        print(super().start())
        return "BRUMHHHHHH !"
    
    
    
b1=Bike("Petrol","BMW","black",5000)
print(b1.color) 
print(b1.fuel_type)
print(b1.custom_start())
print(b1.ride())
print(b1.stop())

