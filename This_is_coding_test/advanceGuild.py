import sys

number = sys.stdin.readline()

numbers = list(map(int,input().split()))

count = 0
res = 0

for i in numbers:
    print(i)
    count +=1
    if count >=i:
        res+=1
        count=0

print("res",res)
print(number)
print(numbers)