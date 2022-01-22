from typing import List

class test:
    def subsets(self, nums: List[int]) -> List[int]:

        # 결과를 받을 빈배열 생성
        res = []

        def dfs(index, path):
            res.append(path)

            print("res", res)
            for i in range(index, len(nums)):
                print("-------------------------------")
                print("iiii",i)
                dfs(i + 1, path + [nums[i]])
                print("path", path, "nums", [nums[i]])

        dfs(0, [])
        return res

test = test()
test.subsets([1, 2, 3])