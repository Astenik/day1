'''this project counts all douplicates of list.'''
lst = [12, 475, 578, 49, 3940]
my_dict = {'count': 0}
for ind in range(len(lst)):
     for ind1 in range(ind + 1, len(lst)):
          if lst[ind] == lst[ind1]:
                  print('num')
                  my_dict['count'] += 1
print(f"count of duplicates is equal to: {my_dict['count']}")
