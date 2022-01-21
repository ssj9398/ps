if __name__ == "__main__":
    s = "hello"
    print(s[1]) # indexing
    print(s[-1]) # indexing reverse order
    print(s[-2]) # indexing
    print(s[1:])  # slicing (***) (substring())
    print(s[1:len(s)]) # slicing index (1 ~ len(s)-1)
    # slicing
    # [start:end] (end 미포함)
    # start <=     < end
    # start: 0 생략
    # end: len(s) 생략

    # in 연산자 (문자열 안에 문자열 포함되는지?)
    print("s" in "str")

    idx = s.index('e') # return index
    print(idx)

    s = "hhhh"
    cnt = s.count('h')
    print(cnt)

    # list, str
    # join: list -> str
    # split: str -> list
    # '1' + '2' + '3'+ '4'
    li = ['1', '2', '3', '4']
    # mutable (수정 가능)
    li[0] = '10'
    s1 = "aa ".join(li)
    print(s1)

    # immutable (수정 불가)
    # s1[0] = '10' # str object does not support item assignment
