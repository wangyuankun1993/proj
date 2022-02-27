tickets = "\nTell me your age, and I will show you the price."
tickets += "\nEnter 'quit' to end the program."
active = True
while active:
    age = input(tickets)
    if age == 'quit':
        active = False
        break
    else:
        if int(age) < 3:
            print("Free.")
        elif int(age) < 12:
            print("The price of ticket is ten dollars.")
        else:
            print("The price of ticket is 15 dollars.")