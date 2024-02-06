""" 
 
animals = ["Zebra","Camel","Ape"]
#start count at 0, reference each element with []
print(animals[0])
for animal in animals:
    print(animal)
 

for animal in animals:
    if (animal == "Camel"):
        print("We're in the desert")


#Strings operate like Lists
x = "Hello Freshman, you all smell"
print(x[0])
y = x.upper()
print(y)

words_list = x.split(",")
print(words_list) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """


""" temp = 57
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
 """

number = input("5")
if (number):
    print("odd")
else:
    print("even")