try:
    numerator = int(input("Enter a number to divide"))
    denominator = int(input("Enter a number to divide by"))
    result = numerator/denominator
    print(result)

except ZeroDivisionError as e:
    print(e)
    print("You can not divide by zero")
except ValueError as e:
    print(e)
    print("Enter only number")
except Exception as e:
    print(e)
    print("something went wrong")

