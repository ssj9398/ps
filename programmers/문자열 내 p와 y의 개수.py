class test:
    def solution(self,s):
        s = s.lower()
        p = 'p'
        y = 'y'
        pCount = s.count(p)
        yCount = s.count(y)
        print(pCount, yCount)
        if pCount == yCount:
            print("true")
        else:
            print("false")

test = test()
test.solution("Pyy")