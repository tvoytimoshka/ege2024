with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\26 (7).txt") as file:
    n = int(file.readline())
    k = int(file.readline())
    m = int(file.readline())
    product = sorted([int(line) for line in file], reverse=True)
    high = 0
    low = n-1
    fridge = 0
    while high <= low:
        free_space = m
        fridge += 1
        while (high <= low) and (product[high] <= free_space):
            free_space -= product[high]
            high += 1
        while (high <= low) and (product[low] <= free_space):
            free_space -= product[low]
            low -= 1
print(fridge, free_space)



