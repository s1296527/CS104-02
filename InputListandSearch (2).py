#List creation and searching
names  = []
n1 = input("enter first name:")
n2 = input ("enter next name:")
names.append(n1)
names.append(n2)
print (names[0])
print (names[1])
search = input("enter search name:")
if search in names:
    print(search, "was found")
else:
    print (search, "was not found")
