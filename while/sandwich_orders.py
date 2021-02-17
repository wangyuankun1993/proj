sandwich_orders = ['pastrami','dried meat floss','vegetables','pastrami','rice','chicken cutlet','pastrami']
finish_sandwiches = []
print("The pastrami has been sell out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finish_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been verified:")
for finish_sandwich in finish_sandwiches:
    print(finish_sandwich.title())