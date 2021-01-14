number = int(input())
factorial = 1
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    if number> 0 and number<10:
        for i in range(1,number + 1):
            factorial = factorial * i
        print(factorial)
