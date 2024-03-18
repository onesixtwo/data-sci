import numpy as vargas

def probA():
    ls = vargas.array([1,2,3,4,5,6,7,8,9,10])
    print("\nArray: \n", ls)
    print("\nAccessing Elements: \n", ls[2])
    print("\nArray Operations: \n", vargas.multiply(ls, 3))
    ls2 = vargas.reshape(ls,(2,5))
    print("\nReshaping Arrays: \n", ls2)
    ls3 = vargas.concatenate((ls,ls))
    print("\nCombining Arrays: \n", vargas.reshape(ls3,(20,1)))


def probB():
    ls = vargas.array([1,3,5,7,9,11,13,15,17,19])
    print("\nOdd Numbers: \n", ls)
    print("\nEven Indices: \n", ls[[0,2,4,6,8]])
    print("\nExponential: \n", vargas.exp(ls))
    ls2 = vargas.reshape(ls,(2,5))
    print("\nTranspose: \n", vargas.transpose(ls2))
    print("\nHorizontatl Concatenation: \n", vargas.concatenate((ls,ls)))

print("\nMain Menu:")
print("1. PROBLEM A")
print("2. PROBLEM B")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    probA()
elif choice == 2:
    probB()
elif choice == 3:
    print("Exiting...")
else:
    print("Invalid choice! Please try again.")