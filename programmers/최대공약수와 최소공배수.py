class test:
    def solution(n, m):
        print(n, m)
        li = []
        for i in range(min(n, m), 0, -1):
            if n % i == 0 and m % i == 0:
                print(i)
                li.append(i)
                break
        for i in range(max(n, m), (m * n) + 1):
            if i % n == 0 and i % m == 0:
                print("i", i)
                li.append(i)
                return li
                break


test = test()
test.solution(3, 12)

