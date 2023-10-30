#Part 1, Question 1
print("Part 1, Question 1\nInteger represents the negetive or positive whole numbers")
eg = int(3)
print(eg,"\n",type(eg))
print("Float means real numbers with demicials")
eg = float(3.1415926535)
print(eg,"\n",type(eg))
print("String represents words or sentences, like a list of characters")
eg = str("Hi, Arash")
print(eg,"\n",type(eg))

#Part 1, Question 2
print("\nPart 1, Question 2\nInput() function is about to ask and let user to input values")
typein = input("Please type your name: ")
print("Hi,",typein)

#Part 1, Question 3
print("\nPart 1, Question 3\nBool is a boolean vairable which means it only contains true or false(1 or 0)")
result_3_3 = bool(3 == 2) #this is about to check if 3 is equal to 2, if it is, it will return a true result,if not, it will return false)
print("The result of if 3 is equal to 2 is", result_3_3)

#Part 1, Question 4
print("\nPart1, Question 4\nvariable assignments means assigning values to variables\n If you want to assign 2 to variable x, you can type x=2\n Let me show you the code\nx=2\nx=3.141592654\nx=\"I am a string\"\nFirstly x is assigned with an integer2\nThen it was assigned with a float 3.141592654\nand the last line of the code, x is assigned with a string")
x=2
x=3.141592654
x="I am a string"

#Part 1, Question 5
print("\nPart 1, Question 5\nThe function type() is to determine the data type of avariable")
print("5,Hello,3.14159\n",type(5),type("Hello"),type(3.14159))

#Part 2, Exercise 1
print("\nPart 2, Exercise 1")
typein = input("Please type your name: ")
print("Hi,",typein)

#Part 2, Exercise 2
print("\nPart 2, Exercise 2")
length_2_2 = float(input("Please input the length of the rectangle: "))
width_2_2 = float(input("Please input the width of the rectangle: "))
print("The area of the rectangle is ",length_2_2*width_2_2)

#Part 2, Exercise 3
print("\nPart 2, Exercise 3")
num = int(input("Please give an integer: "))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")

#Part 2, Exercise 4
print("\nPart 2, Exercise 4")
sum = 0
for x in range(1,11):
    sum += x
print(sum)

#Part 2, Exercise 5
print("\nPart 2, Exercise 5")
temp_cel = float(input("Please input a Celsius temperature: "))
temp_fah = (temp_cel * 9 / 5 ) + 32
print("The Fahrenheit temperature is", temp_fah)

#Part 3, Question 1
print("\nPart 3, Question 1")
print("x+=1 means x = x + 1, x = 1 means assign value 1 to x")
x=0
print("x = 0", x)
x+=1
print("x += 1", x)

#Part 3, Question 2
print("\nPart 3, Question 2")
print("*= means multiply itself and another value")
x= 1
print("x=1",x)
x *= 3
print("x*=3",x)

#Part 3, Question 3
print("\nPart 3, Question 3\n== is used to check if the values of two sides of this operater are equal\nIf they are equal, it will return true or 1, if not, it will return false or 0\n!= do the opposite work")
x=0
y=1
print("x == y", x == y)
print("x != y", x != y)

#Part 3, Question 4
print("\nPart 3, Question 4")
print("< means less than, > means greater than, <= means less or equal to, >= means greater or equal to\nand all these are boolean operaters in python, which will return true or false as a result")
print("1 > 2", 1 > 2)
print("1 >= 1", 1 >= 1)
print("1 < 2", 1 < 2)
print("1 <= 2", 1 <= 2)

#Part 3, Question 5
print("\nPart 3, Question 5")
print("and, or and not are logical operators and they are designed to deal with the logical determining situations")
print("True and False will return a result as", True and False)
print("True or False will return a result as", True or False)
print("not False will return a result as", not False)