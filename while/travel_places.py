travel_places = {}
research = True
while research:
    name = input("\nWhat is your name? ")
    place = input("\nIf you could visit one place in the world, where would you go? ")
    travel_places[name] = place
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        research = False
print("\n---Research Results---")
for name, place in travel_places.items():
    print(name + " would like to go " + place + ".")