x = 121
list_s = str(x)
list_reverse = list(str(x))
list_reverse = list_reverse[::-1]
list_reverse = ''.join(list_reverse)

print(list_s == list_reverse)

