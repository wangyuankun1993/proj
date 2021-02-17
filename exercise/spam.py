def spam(divideBy):
    try:
        return 20 / divideBy
    except ZeroDivisionError:
        print("The divider is zero! Please try another number!")
        
print(spam(10))
print(spam(5))
print(spam(0))
