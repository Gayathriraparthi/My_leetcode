#s = "A man, a plan, a canal: Panama" # output : True
#s = " "  # output : True
s = " race a car"  # output : False
s_list = [ i.lower() for i in s]
s_list1 = []
for i in s_list:
    if i.isalnum() == True:
        s_list1.append(i)
s1 = "".join(s_list1)

print(s1 == s1[::-1])

###
s1 = ""
for i in s:
    if i.isalnum() == True:
        i = i.lower()
        s1 += i
print(s1 == s1[::-1])

###
s1 = [i.lower() for i in s if i.isalnum() == True]
print(s1 == s1[::-1])