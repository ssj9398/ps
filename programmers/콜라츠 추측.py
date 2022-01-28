class test:
    def solution(self,num):
        count =0
        num = int(num)
        while True:
            if count>500:
                return -1
            elif int(num)%2==0:
                num/=2
                count+=1
                print(num)
            elif num==1.0:
                print(count)
                print("끝")
                break
            elif int(num)%2==1:
                num = num *3 +1
                count += 1
                print(num)


test = test()
test.solution(6)