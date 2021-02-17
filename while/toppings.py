toppings = "\nPlease input a series of toppings: "
toppings += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(toppings)
    print(message)
    if message != 'quit':
        print("We will add the " + message + " into the pizza.")