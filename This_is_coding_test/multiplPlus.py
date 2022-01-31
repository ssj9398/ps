a = input()
sum = 0
for i in a:
    print(i)
    if i=='0':
        print("aaaa")
        sum=1
    else:
        sum*=int(i)

print(sum)