'''this project counts how many times every word repeted.'''
my_file = open('file.txt', 'r')
my_file = my_file.read()
names = my_file.split()
my_dict = {f"{names[0]}": 1}
for ind in range(len(names)):
       count = 1
       for ind1 in range(ind + 1, len(names)):
                   if names[ind] == names[ind1]:
                          names.remove(names[ind1])
                          count += 1
       my_dict[f'{names[ind]}'] = count
print(f"count of every word is: {my_dict}")
