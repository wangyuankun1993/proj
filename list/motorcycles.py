motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\n" + "A " + too_expensive.title() + " is too expensive for me.")

guest = ['father','mother','grandma','grandfather']
print("Please come for dinner with me, " + guest[-1] + ".")
absent = guest.pop(3)
print(absent.title() + " " + "cannot come for dinner.")
guest = ['father','mother','grandma','grandfather']
guest[3] = 'uncle'
print(guest)
print("Please come for dinner with me, " + guest[2] + ".")
print("Please come for dinner with me, " + guest[3] + ".")
print("I have found a bigger desk for dinner.")
guest = ['father','mother','grandma','uncle']
guest.insert(0,'brother')
guest.insert(2,'sister')
guest.append('teacher')
print(guest)
print("Sorry that only two guests can come for dinner.")
guest = ['brother', 'father', 'sister', 'mother', 'grandma', 'uncle', 'teacher']
person1 = guest.pop(-1)
print("Sorry that you cannot come for dinner, " + person1.title())
print(guest)
guest = ['brother', 'father', 'sister', 'mother', 'grandma', 'uncle']
person2 = guest.pop(-1)
print("Sorry that you cannot come for dinner, " + person2.title())
print(guest)
guest = ['brother', 'father', 'sister', 'mother', 'grandma']
person3 = guest.pop(-1)
print("Sorry that you cannot come for dinner, " + person3.title())
print(guest)
#guest = ['brother', 'father']
#del guest[0:]
#del guest[0]
#print(guest)
len(guest)
print("The total people invited are " + "len(guest)" + ".")