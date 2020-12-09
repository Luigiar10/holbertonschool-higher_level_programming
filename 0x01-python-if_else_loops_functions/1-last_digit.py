#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
divide = 10
if number < 0:
    divide = -10
ln = number % divide
print('Last digit of {} is '.format(number), end='')
if ln > 5:
    print('{} and is greater than 5'.format(ln))
elif ln < 6 and ln != 0:
    print('{} and is less than 6 and not 0'.format(ln))
else:
    print('{} and is 0'.format(ln))
