def sum_of_dig(num):
      '''this function counts sum of all digits of number.'''
      s = 0
      while num != 0:
           s += num % 10
           num //= 10
      return s 
print(f'the sum of digits of your number is equal to: {sum_of_dig(7364)}')
