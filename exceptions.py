a = 12
s = "hello"

try:
	print("inside try")
	print(a + s) # will raise TypeError
	print("Printed using original data types")

    #print the last n characters
    n = input("Please enter how many characters do you want to read")
    print(s[n:len(s)-1])

    #this instruction will print 12 times the string s
    print(a * s)
    

except TypeError: # will handle only TypeError
	print("inside except")
	print(str(a) + s)
	print("Printed using type-casted data types")

except IndexError: #will handle only IndexError
    print("inside except")
    print('The string has less characters than the number you mentioned')

except IndentationError:
    print('An indentation error detected')






