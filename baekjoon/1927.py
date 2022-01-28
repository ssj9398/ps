import heapq
import sys

inputNumber = int(sys.stdin.readline())
number = [int(input()) for i in range(inputNumber)]

print(number)

res = []
for i in number:
    if i ==0:
        if res:
            print(heapq.heappop(res))
        else:
            print(0)
    else:
        heapq.heappush(res,i)