a = "hello!"
x = a.upper()
list_a = list(a)
first_letter = list_a[0]
first_letter_upper = first_letter.upper()
list_a[0] = first_letter_upper
new_name = "".join(list_a)
print(first_letter,first_letter_upper,new_name) 