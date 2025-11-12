def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key, value)

    print(kwargs["add"])

    print(n)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Audi")
print(my_car.make)
print(my_car.model)
