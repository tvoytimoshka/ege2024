with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\statgrad-ege-inf-14022023-z24.txt") as file:
    max_now = 0
    max_all = 0
    for s in file:
        count = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
                if count > max_now:
                    max_now = count
                    max_all = s.count(s[i])
                if count == max_now:
                    max_all = max(s.count(s[i]), max_all)
            else:
                count = 1
print(max_all)