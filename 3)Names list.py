names =[]
continue_ = True
while continue_:
	name = input ('Type a name: ')
	names.append(name)
	continuar = (input('Do you want to contiune?(Y/N): ') != 'N')

''' or
    names.sort()

for name in names:
    print (name)
'''
'''or

    names.sort()
for idx in range(leg(names)):
    print(str(idx+1),'-',names[idx])

'''
names_in_order = []
while len(names) > 0:
    smaller_idx = 0
    for idx in range(1, len(names)0:
        if (names[idx] < names[menor_idx]):
            smaller_idx = idx
    names_in_order.append(names.pop(smaller_idx))

names = names_in_order

for idx in range(len(names)):
    print (str(idx+1),'-',names[idx])
    