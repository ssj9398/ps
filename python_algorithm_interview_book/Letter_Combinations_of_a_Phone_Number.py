input = input()
#print(input)

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
res = []
li=[]
#for i in range(len(input)):                         # 입력받은 문자의 길이만큼 for문을 돌린다.
    #    for j in numberToEng[input[i]]:                  # 모든 문자열을 반복해 준다.

            #print(i,j)                          # i를 찍어보니까 0 과 1이 나온다
            #print(number[input[i]][0])          # ...... i+1해서 입력한 문자열과 길이가 같으면 apped 해준다.
                                                # 이제 append 해줄껄 만들어보자
            #print(numberToEng[input[0]])
list1 = list(map(str,numberToEng[input[0]]))            # 23을 입력 했을때 2에 해당하는 것을 배열로 만들고
list2 = list(map(str,numberToEng[input[1]]))            # 23을 입력 했을때 3에 해당하는 것을 배열로 만들고
print("만든 배열 찍어보기",list1,list2)
#print(list1[i],list2)
for q in range(3):                              # 번호당 알파벳이 하나라 3개라 for문으로 3번 돌리고
    for w in range(3):
        res = list1[q]+list2[w]                 #list1과 list2를 res에 합쳐준다음
        li.append(res)                          # 합친것을 li에 넣어주었습니다.
        #print("lililili",li)
        #print("res",res)

print(li)
            #print(j,numberToEng[input[i]])
            #print(numberToEng[input[i]][0],numberToEng[input[i]][1])

'''
def letterCombinations(self, digits: str) -> List[str]:
    def dfs(index, path):

        for i in range(index, len(digits)):
            for j in numToEng[digits[i]]:
                dfs(i+1, path+j)

    numToEng={
              "2": "abc",
              "3": "def",
              "4": "ghi",
              "5": "jkl",
              "6": "mno",
              "7": "pqrs",
              "8": "tuv",
              "9": "wxyz"
        }
    res=[]
    return res

letterCombinations("123")
'''



'''
def dfs(index, path):

    if(len(path) == len(digits)):
        res.append(path)
        return

    for i in range(len(digits)):
        for j in number[digits[i]]:
            dfs(i,path)



res = []
'''



''' 스택으로 구현
class Solution:
    def letterCombinations(self, digits: str):


        graph = {
              "2": "abc",
              "3": "def",
              "4": "ghi",
              "5": "jkl",
              "6": "mno",
              "7": "pqrs",
              "8": "tuv",
              "9": "wxyz"
        }

        for i in range(len(digits)):



test = Solution
test.letterCombinations("23")

'''


'''
재귀적으로



class Solution:
    def letterCombinations(self, digits: str):

        def dfs_recursive(node, visited):

            res.append(node)

            for i in range( node, len(digits)):
                for j in number[digits[i]]:
                    dfs_recursive(i,j)


        # 전화번호 딕셔너리
        number = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # 순서대로 방문한 결과를 담을 리스트
        res = []



test = Solution
test.letterCombinations("23")

'''