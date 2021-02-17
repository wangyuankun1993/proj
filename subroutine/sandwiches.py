def make_sandwiches(*toppings):
    print("To make a sandwich, the toppings are list as follows: ")
    for topping in toppings:
        print("- " + topping)

make_sandwiches('vegetable')
make_sandwiches('vegetable', 'fruit')
make_sandwiches('vegetable', 'fruit', 'pepper')