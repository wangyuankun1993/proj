rivers = {
    'yangtze':'china',
    'nile':'egypt',
    'amazon':'brazil',
    }
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print("\n")
for river in sorted(rivers.keys()):
    print(river.title())

print("\nThe follow countries have been mentioned:")
for country in rivers.values():
    print(country.title())