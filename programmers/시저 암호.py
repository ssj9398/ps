class test:
    def solution(self, s, n):
        s = list(s)
        print(s)
        for i in range(len(s)):
            if s[i].isupper():
                s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))

            elif s[i].islower():
                s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

        return "".join(s)


test = test()
test.solution("AB", 1)
