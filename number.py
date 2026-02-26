x = input("please enter the first number: ")
y = input("pleas enter the second number: ")
result = 0
try:
    x = int(x)
    y = float(y)
    result = x / y
except ZeroDivisionError:
    print("you can't divide a numbr by zero")
    exit()
except ValueError:
    print("unable to converto to integer!")
except Exception as e:
    print("unable to proces your request")
else:
    print(f"the result of / is {result}")