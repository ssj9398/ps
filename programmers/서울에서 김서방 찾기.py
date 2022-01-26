class test:
    def solution(self,seoul):
        num=0
        for i in range(len(seoul)):
            print(seoul[i])
            if seoul[i]=="Kim":
                print("kim")
                num =i
        print(num)
        print("김서방은 {}에 있다".format(num))

test = test()
test.solution(["Kim", "Jane"])