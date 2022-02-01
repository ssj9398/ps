inputStr = input()
res = []
number = 0

for i in inputStr:

    if i.isalpha():
        res.append(i)
    else:
        number += int(i)

res.sort()

res.append(str(number))

print(''.join(res))