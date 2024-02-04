with open('"C:\\Users\\Владимир\\Downloads\\24_demo.txt"') as f:
    file = f.readline()

count = 1
max_posl = 0
for i in range(1, len(file)):
    if file[i] != file[i-1]:
        count += 1
    else:
        max_posl = max(max_posl, count)
        count = 1
print(max_posl)

# xyzxyzzzxy