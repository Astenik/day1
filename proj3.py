'''this project counts all douplicates of list.'''
lst = [12, 475, 578, 49, 12, 3940, 12]
my_dict = {f'{lst[0]}': 1}
for ind in range(1, len(lst)):
     num = lst[ind]
     for key in my_dict:
          if key == f'{num}':
             my_dict[f'{num}'] += 1
             break 
     else:
           my_dict[f'{num}'] = 1
print(f"count of duplicates is equal to: {my_dict}")
