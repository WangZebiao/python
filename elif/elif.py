# -*- coding: utf-8 -*-

H = input('input your height')
W = input('input your weight')
Height = int(H)
Weight = int(W)
bmi = Weight/pow(Height,2)
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
else:
    print('pass')
