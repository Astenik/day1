'''this project removes every 3-rd element from the string.'''
string = 'aswtewniwk'
new_string = ''
lst = []
new_string += string[0]
for ind in range(1,len(string)):
       if (ind + 1) % 3 != 0:
             new_string += string[ind]
print(f"your new string is: {new_strin}")
