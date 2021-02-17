my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)

languages = ['C','C++','Python','Java','Perl']
print("The first three items in the list are:")
print(languages[:3])
print("Three items from the middle of the list are:")
print(languages[1:4])
print("The last three items in the list are:")
print(languages[-3:])