kgcm = input('Enter ur weight(kg) and height(cm): ')
kgcm = kgcm.split(' ')
m = float(kgcm.pop()) * 0.01
kg = float(kgcm.pop())

bmi = kg / (m * m)

if 20 <= bmi and bmi < 25:
    print('congrats! yar perfect!')
else:
    print('u need a health care...')