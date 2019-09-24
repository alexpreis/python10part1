myfile = open("fruits.txt")
content = myfile.read()
print (content)
myfile.close()


bfile = open("bear.txt")
content = bfile.read()
print(content[:90])
bfile.close()

with open("fruits.txt","r") as myfile:
    content = myfile.read()

    print(content)
with open("vegetables.txt", "w") as myfilec:
    myfilec.write("Tomato\nCucumber\nOnion\n")
    myfilec.write("Garlic")
    