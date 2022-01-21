from typing import List


class test:
    def subsets(self, nums: List[int]) -> List[int]:
        res=[]

        def dfs(index, path):
            res.append(path)
            print(res)
            for i in range(index,len(nums)):
                print(",,,,,",i+1,path+[nums[i]])
                dfs(i+1,path+[nums[i]])

        dfs(0,[])
        return res


test = test()
test.subsets([1,2,3])