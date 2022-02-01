import sys

n, m = sys.stdin.readline().split()
print(n,m)

numbers = list(map(int,input().split()))
print(numbers)
count = 0
for i in numbers:
    for j in numbers:
        if i>j:
            count+=1
print(count)