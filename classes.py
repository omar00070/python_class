class Car:
    def __init__(self):
        self.number_wheels = 4
        self.color = "black"
        self.motor = "bmw motor"
        self.max_speed = 100
        self.position = 0
        self.direction = "north"

    def move_forward(self):
        self.position += 1
    
    def move_backword(self):
        self.position -= 1 #self.position = self.position - 1
    
    def turn_left(self):
        if self.direction == "north":
            self.direction = "west"
        if self.direction == "west":
            self.direction = "south"
        if self.direction == "south":
            self.direction = "east"
        if self.direction == "east":
            self.direction = "north"

bmw_car = Car()
bmw_car.position

bmw_car.move_backword()
bmw_car.move_backword()

print(bmw_car.color)







