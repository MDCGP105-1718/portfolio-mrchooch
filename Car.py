class Car:
    def __init__(self,colour,manufacturer,model,doors):
        self.colour = colour
        self.manufacturer = manufacturer
        self.model = model
        self.doors = doors

    def PrintDesc(self):
        print("This is a",self.colour,self.manufacturer,self.model,"with",self.doors,"doors.")

Car("Orange","Toyota","Aygo",4).PrintDesc()
