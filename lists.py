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

""" #challenge 1
num = int(input("number:"))
if (num%2):
    print("odd")
else:
    print("even") """


#calculator

bill = input ("Bill:57")
tip = input("Tip:0.1")
ttl = float(bill)+float(tip)
print (ttl) 







""" #challenge 2
bill = float(input ("Bill?"))
service = input("How is the service?")
tp = bill*0
tp1 = bill*0.15
tp2 = bill*0.20
tp3 = bill*0.25

if service == "Bad":
    print(bill+tp)
elif service == "Okay":
    print(bill+tp1)
elif service == "Good":
    print(bill+tp2)
elif service == "Great":
    print(bill+tp3) """