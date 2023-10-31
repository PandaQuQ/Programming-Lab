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