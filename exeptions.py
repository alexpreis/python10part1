def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ("Division by 0")


print(division(1,5))
print(division(1,0))