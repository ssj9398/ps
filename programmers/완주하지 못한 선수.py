class test:
    def solution(self,s):
        li=[]
        words_list = s.split()

        for i in words_list:
            new_word = ""
            for k in range(len(i)):
                new_word += i[k].upper() if k%2==0 else i[k].lower()
            li.append(new_word)
        list = " ".join(li)
        print(list)

test = test()
test.solution("try hello world")