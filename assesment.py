def list_operations():
    my_list = []

    while True:
        print("\nList Operations:")
        print("1. Add element")
        print("2. Remove element")
        print("3. Sort list")
        print("4. Reverse list")
        print("5. Display list")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter element to add: ")
            my_list.append(element)
            print("Element added successfully!")
        elif choice == 2:
            element = input("Enter element to remove: ")
            if element in my_list:
                my_list.remove(element)
                print("Element removed successfully!")
            else:
                print("Element not found in list!")
        elif choice == 3:
            my_list.sort()
            print("List sorted successfully!")
        elif choice == 4:
            my_list.reverse()
            print("List reversed successfully!")
        elif choice == 5:
            print("List:", my_list)
        elif choice == 6:
            break
        else:
            print("Invalid choice! Please try again.")


def tuple_operations():
    my_tuple = ()

    while True:
        print("\nTuple Operations:")
        print("1. Create tuple")
        print("2. Display tuple")
        print("3. Get length of tuple")
        print("4. Access element by index")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = input("Enter elements separated by comma: ").split(',')
            my_tuple = tuple(elements)
            print("Tuple created successfully!")
        elif choice == 2:
            print("Tuple:", my_tuple)
        elif choice == 3:
            print("Length of tuple:", len(my_tuple))
        elif choice == 4:
            index = int(input("Enter index to access: "))
            if 0 <= index < len(my_tuple):
                print("Element at index", index, ":", my_tuple[index])
            else:
                print("Invalid index!")
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")


def set_operations():
    my_set = set()

    while True:
        print("\nSet Operations:")
        print("1. Add element")
        print("2. Remove element")
        print("3. Check if element exists")
        print("4. Display set")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter element to add: ")
            my_set.add(element)
            print("Element added successfully!")
        elif choice == 2:
            element = input("Enter element to remove: ")
            if element in my_set:
                my_set.remove(element)
                print("Element removed successfully!")
            else:
                print("Element not found in set!")
        elif choice == 3:
            element = input("Enter element to check: ")
            if element in my_set:
                print("Element exists in set!")
            else:
                print("Element does not exist in set!")
        elif choice == 4:
            print("Set:", my_set)
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")


def dict_operations():
    my_dict = {}

    while True:
        print("\nDictionary Operations:")
        print("1. Add key-value pair")
        print("2. Remove key-value pair")
        print("3. Get value by key")
        print("4. Display dictionary")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
            print("Key-value pair added successfully!")
        elif choice == 2:
            key = input("Enter key to remove: ")
            if key in my_dict:
                del my_dict[key]
                print("Key-value pair removed successfully!")
            else:
                print("Key not found in dictionary!")
        elif choice == 3:
            key = input("Enter key to get value: ")
            if key in my_dict:
                print("Value:", my_dict[key])
            else:
                print("Key not found in dictionary!")
        elif choice == 4:
            print("Dictionary:", my_dict)
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")


print("\nMain Menu:")
print("1. List Operations")
print("2. Tuple Operations")
print("3. Set Operations")
print("4. Dictionary Operations")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    list_operations()
elif choice == 2:
    tuple_operations()
elif choice == 3:
    set_operations()
elif choice == 4:
    dict_operations()
elif choice == 5:
    print("Exiting...")
else:
    print("Invalid choice! Please try again.")
