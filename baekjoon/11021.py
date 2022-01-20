count = int(input())

for i in range(1,count+1):
    inputNumberA, inputNumberB = map(int,input().split())
    print("Case #%d: %d" %(i,inputNumberA+inputNumberB))