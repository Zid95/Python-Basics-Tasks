#1:create a simple function that takes 2 numbers and print their values
def num(x, y):
    print( x, y)
num(4,2)    
#2:create a simple function that takes 2 numbers and return their values
def num(x, y):
    return x, y
number = num(5, 7)
print(number)


#3:In the above return function, use keyword and arguments when calling the function



#4:In the above return function, give x and y default values of 0 and call the


#5: Create a function that can take any number of args and print the sum of them
def summ(*number):
    result = sum(number)
    return result

example:
x = summ(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(x)
output : 45


#6:create the same sum function using the lambda 
example :

y = (lambda *number: sum(number))(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(y)
output : 45

#7: call lambda on the same line
x = (lambda x, y: x + y)(5, 7)
print(x)


#8:difference between local variable and global variable




