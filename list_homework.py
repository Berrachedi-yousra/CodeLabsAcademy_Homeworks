#Empty list

even_numbers = []

#fill the list with even numbers from 1 to 299 only

for x in range(1, 300):
    if x % 2 == 0:
        even_numbers.append(x)

even_numbers.sort()

#print the lenght of the list

print("The lenght of the list is: ", len(even_numbers))

#print the squared values of the list

print("The squared values of the list: \n")

for x in even_numbers:
    print(x**2, end = ", ")

print("\n")

#check if 57 exists in the list

if(57 in even_numbers):
    print("57 is in the list")
else:
    print("57 is not in the list")

#print(even_numbers)