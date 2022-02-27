class Car():
    def __init__(self, make, model, year):
        self.make_name = make
        self.model_name = model
        self.year_name = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year_name) + ' ' + self.make_name + ' ' +self.model_name
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("The increment odometer is invalid.")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kMh battery.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " +str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_bttery(self):
        self.battery_size.battery_size()

    def get_range(self):
        self.battery_size.get_range()
        

my_tesla = ElectricCar('tesla','model s', 2016)
my_tesla.get_range()
my_tesla.get_range()
