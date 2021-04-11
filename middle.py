x = 10
y = 12
z = 35

print(x, y, z)  # 10 12 35

x = y = z = 10

print(x, y, z)  # 10 10 10

x, y = 10, 23
tmp = x
x = y
y = tmp
print(x, y) # 23 10

x, y = 10, 23
x, y = y, x
print(x, y) # 23 10

test = [1, 2, 3]

print([test, 4, 5])  # [[1, 2, 3], 4, 5]
print([*test, 4, 5])  # [1, 2, 3, 4, 5] 

test = {'apple': 'red', 'remon': 'yellow'}

print({**test,'cherrie': 'pink'}) # {'apple': 'red', 'remon': 'yellow', 'cherrie': 'pink'}

test = 0

if test == 0:
    print('NG')
else:
    print('OK')

test = 0

if not test:
    print('NG')
else:
    print('OK')

test = 'my name is taro' + '.'
test2 = test
print(id(test)) # 140643210401160
print(id(test2))

