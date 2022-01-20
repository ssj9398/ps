import sys

count = input()

for i in range(int(count)):
    inputNumberA, inputNumberB = map(int,sys.stdin.readline().split())
    sum = (inputNumberA + inputNumberB)
    print(sum)