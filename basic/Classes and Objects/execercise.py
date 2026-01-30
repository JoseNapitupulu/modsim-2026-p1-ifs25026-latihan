# define the Vehicle class
class Vehicle:
    
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        
        return desc_str
# your code goes here
car1 = Vehicle ("Fer", "car1", "red", 60.000)
car2 = Vehicle ("Jump", "car2", "blue", 10.000)
# test code
print(car1.description())
print(car2.description())