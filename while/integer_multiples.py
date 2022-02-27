number = input("The number you input is: ")
number = int(number)
if number % 10 == 0:
    print("The number of " + str(number) + " is multiple of ten.")
else:
    print("The number of " + str(number) + " isn't multiple of ten.")