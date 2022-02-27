class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The type of food is " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.restaurant_name + " is on working.")

    def people_number(self):
        print("The " + self.restaurant_name + " has served " + str(self.number_served) + " people.")

    def set_number_served(self, people):
        self.number_served = people

    def increment_number(self, variation):
        self.number_served += variation

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['orange','apple']

    def show_ice(self):
        for i in self.flavors:
            print(i)

restaurant = Restaurant('lanzhouniuroumian', 'north type')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.people_number()
restaurant.set_number_served(100)
restaurant.people_number()

print("\n")

dinner = Restaurant('quanjude', 'beijing type')
dinner.describe_restaurant()
dinner.open_restaurant()
dinner.set_number_served(1000)
dinner.people_number()

dinner.increment_number(200)
dinner.people_number()

print("\n")
my_icecream = IceCreamStand('beijingfandian', 'beijingcai')
my_icecream.show_ice()