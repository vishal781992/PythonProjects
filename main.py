class Car:
    color = ""
    make = ""

    def __init__(self, color, make):
        self.color = color
        self.make = make

    def inWarranty(self, year):
        if year < 2020:
            print("Yes, covers the warranty!")
        else:
            print("out of warranty!")

    def isRepaired(self):
        if "honda" in self.make:
            print("Yes, the car is repaired!")

        else:
            print("Waiting for the response.")

        # self.inWarranty(2021)


def main():
    car = Car("pink", "honda")
    car.isRepaired()
    car.inWarranty(2011)


if __name__ == "__main__":
    main()
