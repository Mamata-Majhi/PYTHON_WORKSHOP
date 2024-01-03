# capitals={
#     "Nepal":"Kathmandu",
#     "China":"Beijing"
# }

# for key,value in capitals.items():
#     print(key,value)


# capitals={
#     "province1":"Biratnagar",
#     "province2":"Janakpur",
#     "province3":"Hetauda",
#     "province4":"Pokhara",
#     "province5":"Butwal",
#     "province6":"Birendranagar",
    
# }
# capitals["province7"]="Dhangadhi"
# # print(capitals)
# print(len(capitals))
# # del capitals["province6"]

# for key,value in capitals.items():
#     print(key,value)

# OOP
# class object 3oops:encapsulation inheritance,polymorphism
class Vehicle:
    # pass
    engine_type="4 stroke"
    transmission="manual"
    def __init__(self,name,brand,color,number_of_seats):
        # function vs method
        # class vitra jati pani function define hunx sapai lai method vaninx
        # pass
        # property:attributes
        self.brand=brand
        self.color=color
        self.name=name
        self.number_of_seats=number_of_seats

    # instance methods
    def start(self):
        print(f"{self.engine_type}Engine started")
    
    def description(self):
        print(f"{self.name},{self.brand},{self.color}")
    
    def stop(self):
        print(f"{self.name}Stopped.")

    def current_speed(self,speed):
        print(f"current speed of {self.name} is {speed}")

Vehicle1=Vehicle(name="vehicle1",brand="Mercedes",color="Black")
Vehicle2=Vehicle(name="vehicle2",brand="Honda",color="Red")
# Vehicle1.start()
Vehicle2.description()
Vehicle1.stop()
Vehicle1.current_speed(100)



# print(Vehicle1.brand)
# print(Vehicle2.color)
# print(Vehicle1.engine_type)
# print(Vehicle2.engine_type)

# inheritance

class AutomaticCar(Vehicle):
    transmission="automatic"

    def __init__(self, name, brand, color, number_of_seats,fuel):
        super().__init__(name, brand, color, number_of_seats)
        self.fuel=fuel


ferrari =AutomaticCar(name="Ferrari",brand="Ferrari",color="black",number_of_seats=4)
ferrari.description()
print(ferrari.transmission())