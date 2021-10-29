#function that checks if a string is a palindrome

print('1- Palindrome function\n')

def ispalindrome(phr):
    return phr == phr[::-1]

choice1 = input('Please enter a string \n')

print(ispalindrome(choice1))

#function that checks if a number is prime or not

print('2- Prime function\n')

def isprime(number):
    prime = True
    i = 2
    for x in range(2, number):
        if number % x == 0: i += 1
    
    if i > 2: prime = False
    return prime

choice2 = input('Please enter a number (positive and greater than 1) \n')

print(isprime(int(choice2)))

#function that checks if a number is in a given range

print('3- Number in range function\n')

def inrange(num, min, max):
    return ((num <= max) and (num >= min))

choice_min = input("Please introduce the min bound of the range\n")
choice_max = input("Please introduce the max bound of the range (greater than the min you introduced before\n")

choice3 = input('What number do you want to check\n')

if (inrange(choice3, choice_min, choice_max)):
    print('The number is in the range [{}, {}]'.format(choice_min, choice_max))
else:
    print('The number is not in the range [{}, {}]'.format(choice_min, choice_max))

#function that calculates the factorial of a number

print('4- Factorial function\n')

def factorial(n):
    result = n
    for x in range(2, n):
        result = result * x
    return result

choice4 = input("Choose a number\n")

print(factorial(int(choice4)))

#function that reverses a string

print('5- String reversing function\n')

def reverse(phr2):
    return phr2[::-1]

choice5 = input('Choose a string to reverse\n')

print(reverse(choice5))

#function to sum all the numbers in a list

print('6- Sum of numbers in list function\n')

list = [5, 3, 8, 9, 10]

def sumlist(list):
    result = 0
    for x in list:
        result = result + x
    return result

print('The sum is {}'.format(sumlist(list)))

#function that finds the max of three numbers

print('7- Max function\n')

def maxthreenumbers(n1, n2, n3):
    return (max(n1, max(n2, n3)))

num1 = input('Please enter the first number ')
num2 = input('Please enter the second number ')
num3 = input('Please enter the third number ')

print('The max number is {}'.format(maxthreenumbers(num1, num2, num3)))