first, second, third = input('Введите 3 числa: \n'), input(), input()
if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else: print('0')
