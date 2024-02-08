#challenge 2
bill = float(input ("Bill?"))
service = input("How is the service?")
tp = bill*0
tp1 = bill*0.15
tp2 = bill*0.20
tp3 = bill*0.25

if service == "bad":
    print(bill+tp)
elif service == "okay":
    print(bill+tp1)
elif service == "good":
    print(bill+tp2)
elif service == "great":
    print(bill+tp3)