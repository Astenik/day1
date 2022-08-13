def  mul_and_sum(num):
           '''this function returns subtraction of mul and sum of digits of number.'''
           s = 0
           m = 1
           while num != 0:
                s += num % 10
                m *= num % 10
                num //= 10
           return (m - s)

print(mul_and_sum(7576869))
