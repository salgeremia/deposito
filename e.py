'''
e = 1 + 1/1! + 1/2! + ... + 1/n!

FOR     -> n = 10
WHILE   -> differenza <= 0.0001
'''

import math

e = 1 
for i in range(1, 11):
    e = e+1/math.factorial(i)
print('FOR ->', e)
    
e = 1 
i = 1
new_e = e+1/math.factorial(i)
differenza = abs(e-new_e)
while differenza > 0.0001:
    i = i+1
    e = new_e
    new_e = new_e+1/math.factorial(i)
    differenza = abs(e-new_e)
print('WHILE ->', new_e)
