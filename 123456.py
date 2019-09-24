import datetime

print("Date & Time is ", datetime.datetime.now())

mynumber = 15
mytext = "Hello world of Pytrhon"

print(mynumber, mytext)
# exersice 1.1

x = 125895474852
print(x)

# exercice 1.2
x = 2
y = 2345
z = "dfffff"
print(x, y, z)

# ex 3
mood = ":-|"
strength = 41.1
rank = 7
print(mood, strength, rank)
print(type(mood), type(strength), type(rank))

# lists
temperature = [9.1, 8.8, 7.5]
students_grades = {"Mary": 9.1, "John": 8.8, "Ivan": 7.5}
mysum = sum(students_grades.values())
length = len(students_grades)
print(mysum / length)

# print (max(students_grades))
# print (students_grades.count(8.777))

username = "Python3"
print(username.lower())

# tuples

monday_temperatures = (1, 4, 5)
print(monday_temperatures)

# apppend

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]

workdays.append(weekend[0])

print(workdays)

# indexing

print(workdays[0:2])
print(workdays[0:])
print(workdays[:2])
print(workdays[-2:0])
print(workdays[-3:-1])
print(workdays[-3:])
print(workdays[:-2])

print('abcdef'[:3])
print(['abc', 'def', 'ghi', 'jkl', 'mno'][-2][-2])


# somthing wrong with functio definition

# def lengther(lst):
#    return len(lst)
#
# l = lengther(2345)
# print('Function is working on workdays' + l)
def myfun(num: object):
    """

    :type num: object
    """
    return num * num


result = myfun(9)
print("My function is working ", result)


def checklenstring(str):
    if len(str) < 8:
        return False
    else:
        return True


print(checklenstring("mypass"))
print(checklenstring("verygoodmypass"))

print("U have to input something by keyboard .....")
user_input = input()
print("Hi there !!!", user_input)
message = "Another variant of output message %s" % user_input
message1 = "Another one {}".format(user_input)
print(message)
print(message1)


def rnName(name):
    """

    :type name: basestring
    """
    return "Hi " + str(name).capitalize()


print(rnName("mAndy"))

colors = [11,11.2,15,15.3,16,17]
for color in colors:
    if int(color)==float(color):
        print (color)


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key,value in phone_numbers.items():
    print("{}: {}".format(key,value))

for value in phone_numbers.values():
        print(value.replace("+","00"))