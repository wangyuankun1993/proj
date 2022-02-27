def make_car(manufacturer, type, **other_info):
    car_info = {}
    car_info ['first'] = manufacturer
    car_info ['second'] = type
    for key, value in other_info.items():
        car_info [key] = value
    return car_info
user_car = make_car('bmw', 'SUV', color = 'blue', tow_package = True)
print(user_car)