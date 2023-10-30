import random as rd
#random_list = []
#for i in range(1,101):
#    random_list.append(rd.randint(1,10))
count = 0
dice = []
for i in range(100):
    dice.append([rd.randint(1,6),rd.randint(1,6)])

for i in dice:
    if i[0]==i[1] and i[0] == 6:
        count += 1
        


print(count)
#print(random_list,len(random_list),random_list.count(2))
