class test:
    def solution(self, numbers, target):
        res=0

        def dfs(index, result):
            if index == len(numbers):
                if result == target:
                    nonlocal res
                    res += 1
                return
            else:
                dfs(index + 1, result + numbers[index])
                dfs(index + 1, result - numbers[index])

        dfs(0, 0)
        print(res)

test = test()
test.solution([1, 1, 1, 1, 1],3)