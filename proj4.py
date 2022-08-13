'''this function counts the count of symbols in file.'''
file = open('file.txt', 'r')
lines = file.readlines()
sum = 0
for line in lines:
      sum += len(line)
print(f"the count of symbols is equal to: {sum}")
