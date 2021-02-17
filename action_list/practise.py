numbers = []
for value in range(1,21):
    numbers.append(value)
print(numbers)

numbers = [value for value in range(1,21)]
print(numbers)

#numbers = [value for value in range(1,1000001)]
#print(numbers)
#print("The min number is " + str(min(numbers)) + ".")
#print("The max number is " + str(max(numbers)) + ".")
#print("The sumary of numbers is " + str(sum(numbers)) + ".")

numbers = [value for value in range(1,21,2)]
print(numbers)

numbers = [value/3 for value in range(3,31)]
print(numbers)

numbers = []
for value in range(1,11):
    triple = value**3
    numbers.append(triple)
print(numbers)

numbers = [value**3 for value in range(1,11)]
print(numbers)