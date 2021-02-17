favorite_numbers = {
    'wangyuankun':[3,5,6],
    'liuchunyu':[1,3,7],
    'liming':[1],
}
for name, numbers in favorite_numbers.items():
    if len(numbers) <= 1 :
        print("\n" + name.title() + "'s favorite number is:")
    else:
        print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))