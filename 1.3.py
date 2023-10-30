name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Panda"]
while True:#some tricky modifications to test the input to avoid numbers
    try:
        user_name = input("Please enter your name: ")
        int(user_name)
        print("I told u to enter a name right?")
    except ValueError:
        break
user_name_upper = user_name.upper()#create a uppercase string of user input, 
user_name[0] = user_name_upper[0]#try to accept the lowercase version of first letter and convert it into upper case

if user_name in name_list:#Check the list
    print("Welcome back,", user_name) #Yes?
else:
    print("Access Denied")# Bye~ 
