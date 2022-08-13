'''this project counts the sum of all numbers in file.'''
file = open('file.txt', 'r')
file = file.read()
nums = file.split()
sum = 0
for num in nums:
     if num.isdigit():
         sum += int(num)
print(f"sum of numbers in file is: {sum}")
