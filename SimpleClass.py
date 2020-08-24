class Chair:
    def __init__(self, height, legs, color="white"):
        self.legs = legs
        self. color = color 
        self.height = height

    

myfirstchair = Chair(1.5, 4, 'red')
print(myfirstchair.legs)
print(myfirstchair.color)
print(myfirstchair.height)

mysecondchair =  Chair(1.7, 5, "white")
print(mysecondchair.legs)
print(mysecondchair.color)
print(mysecondchair.height)

mythirdChair = Chair(1.8, 4)
print(mythirdChair.legs)
print(mythirdChair.color)
print(mythirdChair.height)
