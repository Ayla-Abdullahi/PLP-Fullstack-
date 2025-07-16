# function definition

def greet(name):
    print("hello",name)



#function call

greet("Ayla")

# function with return value
def add_numbers(a, b):
    return a + b



# function call with return value
result = add_numbers(5, 10)
print("The sum is:", result)    



#function to check if a number is even or odd
def Check_odd_even(number):
    if number % 2 == 0:
        return number, "is even"
    else:
        return number,"is odd"
    

# function call to check if a number is even or odd
number=int (input("enter your number: "))
result= Check_odd_even(number)
print(result[0], result[1])