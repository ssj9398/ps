## 배열 파티션
from typing import List
def isPalindrome(strt : List[int]):
    strt.sort()

    print(sum(strt[::2]))



if __name__ == "__main__":
    isPalindrome([1, 4, 3, 2,1,7])
