f = input('First Name: ')
l = input('Last Name: ')
c = input('Company Website: ')

print('')
print('Possible Email Address:')
print('')

print(f'{f}@{c}')
print(f'{f}{l}@{c}')
print(f'{f}{l[0]}@{c}')
print(f'{f[0]}{l}@{c}')
print(f'{f}{l[0]}@{c}')
print(f'{f}.{l}@{c}')
print(f'{l}.{f}@{c}')
print(f'{f[0]}.{l}@{c}')
print(f'{f}.{l[0]}@{c}')
print(f'{f}_{l}@{c}')
print(f'{l}_{f}@{c}')
print(f'{f[0]}_{l}@{c}')
print(f'{f}_{l[0]}@{c}')
print(f'{f}-{l}@{c}')
print(f'{l}-{f}@{c}')
print(f'{f[0]}-{l}@{c}')
print(f'{f}-{l[0]}@{c}')

