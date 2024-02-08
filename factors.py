#Create a function that accepts an input and determines all factors of the number.
#This function factors() takes an integer input number.
#It iterates through numbers from 1 to number, checking if each number divides number evenly (i.e., with no remainder).
#If so, it appends that number to the list of factors.


def factors(numb):
   factors = []
   for i in range(1, numb+1):
       if numb % i == 0:
          factors.append(i) 
       return factors
num = int(input("Enter a number:"))
print("Factors of", num, "are:", factors(num))


