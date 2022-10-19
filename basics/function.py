def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        result = "fizz_buzz"
        return result
    elif input % 3 == 0:
        result = "fizz"
        return result
    elif input % 5 == 0:
        result = "buzz"
        return result
    else:
        return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(17))
