print('DECIMAL NUMEBER ADDER')
print('--- type EXIT to leave ---')
total = 0
while True:
    value = input('Type a decimal number: ')
    if value == 'EXIT':
        break
    try:
        total = total + float(value)
    except:
        pass
    print ('Value =', total)
