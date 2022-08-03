from ast import If
from msilib.schema import Condition
from pickle import FALSE, TRUE


# Condition-------------------------------------------
a = 2
b = 3
if a > b:
    print(b, 'is greater than ', a)
else:
    print('something')


# or and------------------------------------------------------
boy = False
short = True

if boy and short:
    print('He is a boy and short')
elif boy or short:
    print('He is a boy or not short')
else:
    print('nothing...............')
