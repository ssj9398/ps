import sys
while True:
    numberA, numberb = map(int,sys.stdin.readline().split())
    if numberA==0 and numberb ==0:
        break

    print(numberA+numberb)