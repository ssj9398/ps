num1, num2 = map(int,(input().split()))

num1 *= 60
sum = num1 + num2   # 전체시간 계산
rs = sum - 45        #45분 이전 총시간 계산

a = int(rs/60)     #45분 이전 시간 계산

rs2 =  rs - a * 60
if sum <45:
    a = 23
    rs2 +=60

print(a, rs2)