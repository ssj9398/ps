class test:
    def solution(self,x):
        li=[]
        sum = 0
        for i in str(x):
            li.append(i)

        for i in li:
            print("iiii",i)
            sum += int(i)
        print(sum)
        print(li)
        if x%sum==0:
            print(True)
        else:
            print(False)
test = test()
test.solution(10)