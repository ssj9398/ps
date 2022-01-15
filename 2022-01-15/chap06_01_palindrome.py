## 유효한 팰린드롬

def isPalindrome(str):
    for i in range(len(str)//2):
        j = len(str)-1-i
        if str[i] == str[j]:
            print("앞뒤가 똑같음")
        else:
            print("다른거임")


if __name__ == "__main__":
    isPalindrome("aab")