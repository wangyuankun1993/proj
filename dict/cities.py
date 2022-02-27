cities = {
    'lanzhou':{
        'country':'china',
        'population':'3 million',
        'fact':'old city',
        },
    'tokyo':{
        'country':'japan',
        'population':'10 million',
        'fact':'beautiful city',
        },
    'newyork':{
        'country':'american',
        'population':'20 million',
        'fact':'freedom',
        },
    }
for city, city_info in cities.items():
    print(city.title())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + city_info['population'])
    print("\tFact: " + city_info['fact'].title())