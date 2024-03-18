import numpy as nop

def act1():
   lst = nop.array([1,2,3,4,5,6,7,8,9,10])
   print("Numberr list:", lst)
   print("1. Addition\n"
      "2. Subtraction\n"
      "3. Division\n"
      "4. Multiplication\n"
      "5. Get Array Mean\n"
      "6. Get Array Median\n"
      "7. Get Array Mode")

   ch = int(input("choose a number: "))

   if ch == 1:
      print("All Array Added: ",nop.sum(lst))
   elif ch == 2:
      sub = float(input("number to subtract in the Array: "))
      print("Result of Subtraction: ", nop.subtract(lst, sub))
   elif ch == 3:
      div = float(input("number to divide in the Array: "))
      print("Result of Subtraction: ", nop.divide(lst, div))
   elif ch == 4:
      mul = float(input("number to multiply in the Array: "))
      print("Result of Subtraction: ", nop.multiply(lst, mul))
   elif ch == 5:
      print("The Mean is: ", nop.mean(lst))
   elif ch == 6:
      print("The Median is: ",nop.median(lst))
   elif ch == 7:
      print("The Mode is: ",nop.argmax(nop.bincount(lst)))
   else:
      print("Wrong choice!")


def act2():
   print("Input a 10 number for the array one by one")
   lst2 = []
   for _ in range(10):
      item = int(input("Enter a number: "))
      lst2.append(item)

   print("Number list:", lst2)
   print("1. Addition\n"
         "2. Subtraction\n"
         "3. Division\n"
         "4. Multiplication\n"
         "5. Get Array Mean\n"
         "6. Get Array Median\n"
         "7. Get Array Mode")

   ch = int(input("Choose a number: "))

   if ch == 1:
      print("All Array Added: ", nop.sum(lst2))
   elif ch == 2:
      sub = float(input("Number to subtract in the Array: "))
      print("Result of Subtraction: ", nop.subtract(lst2, sub))
   elif ch == 3:
        div = float(input("Number to divide in the Array: "))
        print("Result of Division: ", nop.divide(lst2, div))
   elif ch == 4:
      mul = float(input("Number to multiply in the Array: "))
      print("Result of Multiplication: ", nop.multiply(lst2, mul))
   elif ch == 5:
      print("The Mean is: ", nop.mean(lst2))
   elif ch == 6:
      print("The Median is: ", nop.median(lst2))
   elif ch == 7:
      print("The Mode is: ", nop.argmax(nop.bincount(lst2)))
   else:
      print("Wrong choice!")


print("\n\nASSIGNMENT: MACHINE PROBLEMS - NUMPY | VARGAS, JOHN KENNETH COE 003 - CPE22S3\n\n")

print("1. Act no.1\n"
      "2. Act no.2\n")

ch1 = int(input("choose a number: "))

if ch1 == 1:
   act1()
elif ch1 == 2:
   act2()
else:
   print("Wrong choice!")

