#requested_toppings = ['mushroom','extra cheese']
#if 'mushroom' in requested_toppings:
    #print("Adding mushroom.")
#elif 'pepperoni' in requested_toppings:
#if 'pepperoni' in requested_toppings:
    #print("Adding pepperoni")
#elif 'extra cheese' in requested_toppings:
#if 'extra cheese' in requested_toppings:
    #print("Adding extra ")

#print("\nFinished making your pizza!")
'''
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")
'''
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','frech fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")