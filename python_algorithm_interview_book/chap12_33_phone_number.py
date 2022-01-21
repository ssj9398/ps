from typing import List

class test:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        numberToEng = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(index, path):
            if len(digits) == len(path):
                print(path)
                res.append(path)
                return

            for i in range(index, len(digits)):
                for j in numberToEng[digits[i]]:
                    #print(i+1, j+path)
                    dfs(i+1, path+j)
        print(res)

        dfs(0,"")
        return res

test = test()
test.letterCombinations("23")
