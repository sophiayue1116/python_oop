# encapsulation in python
# private, protected and public
# In Python there is not private attributes, you can't protect them. only for convention

class Car:
    # public attr, accessible by any class
    noOfwheels = 4
    # protected attr, accessible by this class and any derived class
    _color = "Black"
    # private attr, accessible only by this class
    __secretcode = "007"

class Mazda(Car):
    def __init__(self):
        print("Protected Attribute Color: ", self._color)

if __name__ == "__main__":
    car = Car()
    print("Public attribute number of wheels: ", car.noOfwheels )
    print("Protected attribute color of car: ", car._color )
    #print("Private attribute secretcode of car: ", car.__secretcode ) # In Python there is not private attributes, you can't protect them.
    mazda = Mazda()

