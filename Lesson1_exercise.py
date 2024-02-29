"""
Exercise 1
Write a program that will ask the user to enter three numbers and then return the sum
"""
firstnumber=int(input("Please enter the first number"))
secondnumber=int(input("Please enter the second number"))
thirdnumber=int(input("Please enter the third number"))
sum=firstnumber+secondnumber+thirdnumber
print("The sum of the three numbers is ",sum)

"""
Exercise 2
Asks the user to input 2 numbers and
then perform the following mathematical operation on those two numbers: +, -, *, /, %, //, **.
then, for each operation print out the operation name and the result.
"""
firstnumber=int(input("Please enter the first number"))
secondnumber=int(input("Please enter the second number"))
firstnumber+secondnumber
firstnumber-secondnumber
firstnumber*secondnumber
firstnumber/secondnumber
firstnumber%secondnumber
firstnumber//secondnumber
firstnumber**secondnumber
type(firstnumber+secondnumber)

"""
Exercise 3
What will be the result of the following python operations?
0 / 4
4 / 0
"""

"""
Exercise 4
Correct these lines of code using type conversion. Then print the calculated resulat of all three variables and their data type.
price_3_books = '5.0' * 3
my_age = 'I am ' + 26
total_bill = 4.45 + 3.30 + 6 + '7'
"""
price_3_books = float('5.0') * 3
print(price_3_books)
type(price_3_books)

my_age = 'I am ' + str(26)
print(my_age)
type(my_age)

total_bill = 4.45 + 3.30 + 6 + 7
print(total_bill)
type(total_bill)


"""
Exercise 5
Suppose your teacher wants to calculate your average grade, based on three grades that it gave you for an assignment. Make the python script that can calculate the avearge of three numbers:
ask the user three times to input a number (assignment grade)
convert the input to the correct data type and assign them to variables
calculate the average of the three numbers
print the average to the screen (which data type do you need to correctly calculate an average of numbers?)
provide your code with usefull comments
"""


"""
Exercise 6: String Concatenation

Create two variables first_name and last_name and assign them your first and last names.
Print your full name using string concatenation.
"""


"""
Exercise 7: Type Conversion

Given the string num_str = "42" and the integer factor = 3.
Convert num_str to an integer and calculate its product with factor.
Print the result.
"""


"""
Exercise 8: Combining Strings and Numbers

Create a variable age and assign it your age as an integer.
Create a variable message that says: "I am X years old." Replace X with the value of age.
Print the message.
"""


"""
Exercise 9: Variables and Basic Arithmetic

Create two variables num1 and num2 and assign them any integer values.
Print the sum, difference, product, and quotient of num1 and num2.
"""


"""
Exercise 10: Working with Floats

Ask the user to enter the radius of a circle (use input()).
Convert the input to a float and calculate the area of the circle
(Area = (π * radius) * (π * radius)).
π is the constant pi (3.14159).
Print the area.
"""


"""
Exercise 11: Combining Strings and Operators

Ask the user to enter their name (use input()).
Create a welcome message with their name using string concatenation (e.g., "Welcome, John!").
Print the welcome message.
"""


"""
Exercise 12: User Input and Arithmetic

Ask the user to enter two numbers (use input() to receive input).
Convert the input strings to integers and assign them to variables.
Calculate and print the sum and product of the two numbers.
"""


"""
Exercise 13: Temperature Conversion

Ask the user to enter a temperature in Celsius (use input()).
Convert the input to a float and calculate the temperature in Fahrenheit (F = C * 9/5 + 32).
Print the temperature in Fahrenheit.
"""


"""
Exercise 14: Length of String
Instruction:

Ask the user to enter a word or a sentence using input().
Calculate and print the length of the input string.
"""


"""
Exercise 15: Integer Division and Remainder
Instruction:

Ask the user to enter two integers (numerator and denominator) using input().
Convert the input to integers and calculate the result of integer division and the remainder.
Print the quotient and remainder.
"""