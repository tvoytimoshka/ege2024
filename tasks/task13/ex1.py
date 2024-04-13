from itertools import product

count = 0
for i in product("01", repeat=13):
    ip_address = ('1' * 9) + ''.join(i)
    print(i)
    if ip_address.count('1') % 4 == 0:
        count += 1
print(count)
