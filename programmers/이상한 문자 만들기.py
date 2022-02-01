class test:
    def solution(self, s):
        words_list = s.split(' ')
        print(words_list)
        new_list = []
        for word in words_list:
            new_words = ""
            for i in range(len(word)):
                new_words += word[i].upper() if i%2 == 0 else word[i].lower()
            new_list.append(new_words)
        print(" ".join(new_list))

test = test()
test.solution("try hello world")