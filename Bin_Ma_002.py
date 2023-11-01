#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Bin Ma
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 1
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random as rd

flag_1 = 0
flag_2 = 0
while flag_1 == 0:
        while flag_2 == 0:
            try:
                a = int(input("Part 1\nPlease enter an integer between 1 and 100: "))#ask user to enter the integer
                flag_1 = 1
                if (a>=1 and a<=100): #(a
                    flag_2 = 1
                    print("a)",a,"is between 1 and 100") #(a
                    a_sqrot = a**0.5 #find the square root of the given number
                    if(1<a <=3):
                        print("b)",a,"is a prime number") #to start from 3
                    elif(a == 1):
                        print("b)",a,"is not a prime number") #avoid 1
                    else:
                        #a_sqrot+(21%5>0) means it can be sure that this value can be sure be used for int(equal or +1 to the original)
                        for x in range(2,int(a_sqrot+(21 % 5 > 0))): #if the number is prime, there must be a factor number within the range of its square root
                            if (a % x == 0):  #(b, (c
                                print("b)",a,"is not a prime number")  #get it!
                                if(a%2==0):
                                    smallest_factor = 2
                                elif(a%3==0):
                                    smallest_factor = 3
                                elif(a%a_sqrot==0):
                                    smallest_factor = a_sqrot
                                print("c) The smallest prime factor is ",int(smallest_factor))
                                break
                        else:#this else can be tricky, because it follows the 'for' loop with break
                            print("b)",a,"is a prime number")
            except ValueError:
                print("What did u typed in? I told u already u should enter an INTEGER")
                    
            else:
                print("a)",a,"is not between 1 and 100") #(a

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 2
#a)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
flag_2 = 0
while flag_2 == 0:
    try:
        age = int(input("Part 2 a)\nPlease enter your age(Integer): "))#acquire user's age
        flag_2 = 1
        #Design a license which can upgrade automatically according to the owner's age(?????)
        #5 for bicycles, 15 for motorcycles, 18 for cars, 25 for commercial trucks and 80 for expiration
        if(age >= 5 and age < 80 ):# 1st detection for the age(5<age<80)
            status_checked = False
            while(status_checked == False): #a while loop for check if the input is correct
                obtain_str_license = str(input("Do you have a driver license?(y/Y/Yes/yes/YES) "))
                if(obtain_str_license == "Y" or obtain_str_license == "Yes" or obtain_str_license == "yes" or obtain_str_license == "YES" or obtain_str_license == "y"):
                    status_license = True
                    status_checked = True
                elif(obtain_str_license == "N" or obtain_str_license == "No" or obtain_str_license == "no" or obtain_str_license == "NO" or obtain_str_license =="n"):
                    status_license = False
                    status_checked = True
                else:
                    print("Please enter your driver license status properly: For yes you can type in \'Yes\',\'Y\',\'n\',\'YES\',\'yes\'")
                    status_checked = False

            if(status_license):#✔ or ✖ for different ages
                if(age>= 5):
                    print("Bicycle License          ✔")
                if(age>=15):
                    print("Motorcycle License       ✔")
                else:
                    print("Motorcycle License       ✖")
                if(age>=18):
                    print("Car License              ✔")
                else:
                    print("Car License              ✖")
                if(age>=25):
                    print("Commercial Truck Lisence ✔")
                else:
                    print("Commercial Truck Lisence ✖")

            else:
                #no license? what r u doing here?
                print("You don't have a license, why waste your time to check?")

        else:
            print("You're too young or too old for driving!")
    except ValueError:
        print("What did u typed in? I told u already u should enter an INTEGER")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#(b
#-----------------------------------------------------------------------
# FLOWCHART
#-----------------------------------------------------------------------
#                ---------
#               (  Start  )
#                ---------
#                    |
#                    |
#           -------------------
#           | initial 2 flags |
#           | and 3 viriables |
#           | cw_score and    |
#           | exam_score and  |
#           | and total_score |
#           -------------------
#                    |
#                    |
#              ------------------
#             / Ask user to    /    
#            / input cw_score /   <---------
#           / and exam_score /             |
#          ------------------              |
#                    |                     |
#                    |                     |
#                    /\                    |
#                  /    \                  |  No
#                /        \                |
#              /            \              |
#            /                \            |
#          /                    \          |
#        /   0<= cw_score <= 50 ? \---------
#         \ 0<= exam_score<=50 ? /
#           \                  /           
#             \              /             
#               \          /               
#                 \      /                 
#                   \  /                   
#                    \/                    
#                    |                     
#                 Yes|                     
#                    |                     
#                    /\
#                  /    \
#                /        \
#              /            \
#            /                \     No
#          /   cw_score >= 20?  \-----------
#           \                  /           |
#             \              /             |
#               \          /               |
#                 \      /                 |
#                   \  /                   |
#                    \/                    |
#                    |                     |
#                 Yes|                     |
#                    |           ----------------------
#                    |<----------| tech_fail_flag = 1 |
#                    |           ----------------------
#                    /\
#                  /    \
#                /        \
#              /            \
#            /                \     No
#          / exam_score >= 20? \-----------
#           \                  /           |
#             \              /             |
#               \          /               |
#                 \      /                 |
#                   \  /                   |
#                    \/                    |
#                    |                     |
#                 Yes|                     |
#                    |           ----------------------
#                    |<----------| tech_fail_flag = 1 |
#                    |           ----------------------
#                    |
#                    /\
#                  /    \
#                /        \
#              /            \
#            /   exam_score   \     No
#          /          +         \-----------
#           \     cw_score     /           |
#             \     >=45?    /             |
#               \          /               |
#                 \      /                 |
#                   \  /                   |
#                    \/                    |
#                    |                     |
#                 Yes|                     |
#                    |                     /\
#                    |                   /    \
#                    |                 /        \
#                    |               /            \
#                    |             /   exam_score   \     No
#                    |           /          +         \-----------
#                    |            \     cw_score     /           |
#                    |              \     >=44?    /             |
#                    |                \          /               |
#                    |                  \      /                 |
#                    |                    \  /                   |
#                    |                     \/                    |
#                    |                  Yes|                     |
#                    |                     |          -----------------------
#                    |                     |          | grade_fail_flag = 1 |
#                    |                     |          -----------------------
#                    |                     |      
#                    |      ---------------------------------
#                    |      | print Your finall score is 45 |
#                    |      ---------------------------------
#                    |
#                    /\
#                  /    \
#                /        \
#              /            \
#            /                \     No
#          /grade_fail_flag ?=0 \-----------
#           \                  /           |
#             \              /             |
#               \          /               |
#                 \      /                 |
#                   \  /                   |
#                    \/                    |
#                    |                     |
#                 Yes|                     |
#                    |    ----------------------------------------
#                    |    | print failed and exam_score+cw_score |
#                    |    ----------------------------------------
#                    |
#                    |
#                    /\
#                  /    \
#                /        \
#              /            \
#            /                \     No
#          / tech_fail_flag ?=0 \-----------
#           \                  /           |
#             \              /             |
#               \          /               |
#                 \      /                 |
#                   \  /                   |
#                    \/                    |
#                    |                     |
#                 Yes|                     |
#                    |           -----------------------
#                    |           | print failed and 44 |
#                    |           -----------------------
#                    |
# ----------------------------------------
# | print passed and exam_score+cw_score |
# ----------------------------------------
#                    |
#                    |
#               -----------
#              (   Stop    )
#               -----------
#-----------------------------------------------------------------------
# pseudo-code
#-----------------------------------------------------------------------
# int cw_score,exam_score,tech_fail_flag=0,grade_fail_flag=1
# get_input:
#     input cw_score, exam_score
#     if 0<=cw_score<=50 && 0<=exam_score<=50
#         if cw_score < 20 || exam_score < 20
#             tech_fail_flag = 1
#         if exam_score+cw_score<45
#             if exam_score+cw_score>=44
#                 print("Passed! Your final score is 45")
#             else
#                 grade_fail_flag = 1
#                 print ("Failed", exam_score+cw_score)
#         if grade_fail_flag == 0 && tech_fail_flag == 0
#             print ("Passed!", exam_score+cw_score)
#     else
#         goto get_input
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Part2, b)")
tech_fail_flag = 0
grade_fail_flag = 0
correct_input_flag = 0
while correct_input_flag == 0:
    try: #check the input
        cw_score = float(input("Please enter your coursework score: "))
        exam_score = float(input("Please enter your exam score: "))
        if (0 <= cw_score <= 50) and (0 <= exam_score <= 50):
            correct_input_flag = 1 #got correct input
            if(cw_score <20) or (exam_score < 20):
                tech_fail_flag = 1 #check techinial failed
            if exam_score + cw_score < 45:
                if exam_score + cw_score >= 44:
                    print("Passed! Your final score is 45") #round up for over 44 and no technical fail
                else:
                    grade_fail_flag = 1
                    print("Failed! Your final score is ",exam_score + cw_score) #Simply failed, such a waste
            if grade_fail_flag == 0 and tech_fail_flag == 0:
                print("Passed! Your final score is ", exam_score + cw_score)# Normal passed, whatever
        else:
            raise ValueError #check if the number is over 50
    except ValueError:
        print("Input Error! Please enter the correct score")# Can't people just type in the write number?
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part3 Q3.1
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#a) the expression of this is (-1)(-2)^x, 1<=x<=20, x is integer
print("Part 3, Q3.1, a)")
list_a = []
for x in range(1,21):
    list_a.append((-1)*(-2)**x)
print(list_a)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#b) the expression of this is x = x + y , y is 2k-1 , 1<=k<=49
print("Part 3, Q3.1, b)")
list_b = []
result = 1
for x in range(1,50):
    result += 2*x -1
    list_b.append(result)
print(list_b)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#c)this is a tricky one, if u try to solve it in math way it could be hard, but
#if you just think about appending the odd index number as 1234 and even index as 1
#this can be easier
print("Part 3, Q3.1, c)")
list_c = []
for x in range(1,201):
    if x%2 == 0:
        list_c.append(1)
    else:
        list_c.append(int(x/2+0.5))
print(list_c)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 3, Q3.2
print("Part 3, Q3.2")#easy one
genral_list_x = list(range(0,101))#generate a general list
print("General list x\n" , genral_list_x)#show the list
odd_list = [] #create all 3 lists
even_list = []
not_div_by_5 = []
for x in range(len(genral_list_x)): #Let's freaking do the job
    if x % 2 != 0:#if the index is odd, add it to the odd_list
        odd_list.append(genral_list_x[x])
    else:#if the index is even, add it to the even_list
        even_list.append(genral_list_x[x])
    if x % 5 != 0:#if the index is not divisible by 5, add it to the not_div_by_5
        not_div_by_5.append(genral_list_x[x])
print("a)odd indices\n",odd_list,"\nb)even indices\n",even_list,"\nc)not divisible by 5 indices\n",not_div_by_5)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 3, Q3.3
print("Part 3, Q3.3")#another easy one
grade_list=[85, 92, 78, 90, 88, 76, 89, 80, 94, 87]#using the given list
grade_list.remove(min(grade_list))#remove the lowest
grade_list.remove(max(grade_list))#remove the highest
#print(grade_list) #debug
sum = 0
for x in grade_list:#build a loop to calculate the sum
    sum += x
print("The average of these grades excluing the lowest and highest grade is", sum/len(grade_list))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 4, Q4.1
#Why this is getting easier and easier
#oh that may be I am way much more familiar with Python
print("Part 4, Q4.1")#Finally! Part 4!
while True:#Now I found a shorter way to build this checking loop
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("I told u to enter an INTEGER right?")
for x in range(1,n+1):#simply build a loop for repeating things
    print(str(x)*x,end=" ")
print("\n")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 4, Q4.2
#a)
print("Part 4, Q4.2")#2 more questions!
#this expression is about to caculate the sum of (-2)^k where 0<=k<=5 k is an integer
sum_a = 0 #Initial a sum for question a
for k in range(0,6):#build a loop from 0 to 5
    sum_a+=(-2)**k#do the simple math
print("a)",sum_a)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#b) just modify some arguments from question a 
sum_b = 0 #Initial a sum for question b
for k in range(-5,1):#build a loop from -5 to 0
    sum_b+=(-2)**k#do the simple math
print("b)",sum_b)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#c) oh is it a simple sum_a + sum_b? let's see
#sum_c1 = 0 #Initial a sum for question c in traditional way
#for k in range(-5,6):#build a loop from -5 to 5
#    sum_c1+=(-2)**k#do the simple math
#print("c)",sum_c1)
print("c)",sum_a+sum_b-(-2)**0)#because (-2)**0 will be added twice
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 4, Q4.3
print("Part 4, Q4.3")#Only one question left!!!!!!
#we need random package for this
score = 10 #initial a limit for attempt times and use is for score also
random_number=rd.randint(1,100)#generate a random integer from 0 to 100
#print(random_number)#Debug
while score != 0:
    while True:#old ways innit?
        try:
            user_input = int(input("Please take a guess(integer)(0-100): "))
#            print(score)#Debug
            break
        except ValueError:
            print("I told u to enter an INTEGER right?")
    if(user_input == random_number):#let's see how user take a guess
        print("Bingo! You get the right answer, the number is", random_number, "\nYour score is" , score)
        break  #Correct! end this boring program
    elif(user_input - random_number > 10):
        #if the answer is 10 greater than the random number
        score -= 1# HP - 1
        print("Take another guess? Your answer is way too high, your score is" , score)

    elif(10 >= (user_input - random_number) > 0):
        #if the answer is greater than but close enough to the random number
        score -= 1# HP - 1
        print("Take another guess? Your answer is high but close, your score is" , score)
        
    elif( (random_number - user_input) > 10):
        #if the answer is 10 less than the random number
        score -= 1# HP - 1
        print("Take another guess? Your answer is way too low, your score is" , score)
        
    elif(10 >= (random_number - user_input) > 0):
        #if the answer is less than but close enough to the random number
        score -= 1# HP - 1
        print("Take another guess? Your answer is low but close, your score is" , score)
if score == 0:
    print("You failed bruh~, 0~")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 4, Q4.4
print("Part 4, Q4.4")#The final one!!!!!
name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Panda"]
while True:#some tricky modifications to test the input to avoid numbers
    try:
        user_name = input("Please enter your name(First letter uppercase nonsensitive): ")
        int(user_name)
        print("I told u to enter a name right?")
    except ValueError:
        break
user_name_upper = list(user_name)#create a uppercase string of user input, 
user_name_upper[0] = user_name_upper[0].upper()
user_name = "".join(user_name_upper)#try to accept the lowercase version of first letter and convert it into upper case
if user_name in name_list:#Check the list
    print("Welcome back,", user_name) #Yes?
else:
    print("Access Denied")# Bye~ 