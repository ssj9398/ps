import sys

numberA, numberB = map(int,sys.stdin.readline().split())
c = map(int,sys.stdin.readline().split())

for i in c:
    if i < numberB:
        print(i, end=" ")
