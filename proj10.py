def odd_nums(num1, num2):
      '''this function counts the count of odd numbers in interval (num1, num2).'''
      ind = num1
      count = 0
      while ind <= num2:
            if ind % 2 != 0:
                 count += 1
            ind += 1 
      return count

print(f"the count of odd numbers in interval (1, 9) is: {odd_nums(1, 9)}")
