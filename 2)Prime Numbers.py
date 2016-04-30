print ('------Números primos-----')
print ('-------X para sair-------')
while True:
    num = input('Digite o número: ')
    if (num)=='X':
        print ('Saindo')
        break
    num = int(num)
    for x in range(2,num):
        if (num%x) == 0:
            print ('Número nao é primo.')
            break
        else:
            print ('Esse é primo.')
            break
