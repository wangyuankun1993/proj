my_foods = ['pizza','noodle','hamberger','roujiamo']
for food in my_foods[:]:
    print(food)
print("\n")
friend_foods = my_foods[:]
for food in friend_foods[:]:
    print(food)
print("\n")
my_foods.append('tomato')
friend_foods.append('potato')
print("My favourite foods are:")
for food in my_foods[:]:
    print(food)

print("My friend's favourite foods are:")
for food in friend_foods[:]:
    print(food)