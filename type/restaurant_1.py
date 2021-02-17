from restaurant import Restaurant

restaurant1 = Restaurant('A','B')
print(restaurant1.restaurant_name + " " + restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print(restaurant1.number_served())
restaurant1.people_number(2)
print(restaurant1.number_served())
restaurant1.increment_number(10)