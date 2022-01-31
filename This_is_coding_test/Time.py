import sys
import time

number = int(sys.stdin.readline())
count = 0
print(number)
for i in range(number+1):
    for j in range(60):
        for k in range(60):
            print(i,j,k)
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                count +=1
                print("카운트 증가")
print(time.time())
print("count = ",count)