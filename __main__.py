first = int(input('введите число'))
second = int(input('введите число'))
third = int(input('введите число'))
if first == second and first == third and second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second and first != third and second != third:
    print('0')