def get_formatted_city(city, country, population=''):
    if population:
        full_city = city + ', ' + country + ' - population ' + population
    else:
        full_city = city + ', ' + country
    return full_city.title()