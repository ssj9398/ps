class test:
    def solution(self,dirs):
        li = []
        count = 0
        x, y = 0, 0

        for i in dirs:

            if i == 'U':
                x2, y2 = x, y + 1
                if y2 <= 5:
                    if (x, y, x2, y2) not in li:
                        li.append((x2, y2, x, y))
                        li.append((x, y, x2, y2))
                        count += 1
            elif i == 'L':
                x2, y2 = x - 1, y
                if x2 >= -5:
                    if (x, y, x2, y2) not in li:
                        li.append((x2, y2, x, y))
                        li.append((x, y, x2, y2))
                        count += 1
            elif i == 'R':
                x2, y2 = x + 1, y
                if x2 <= 5:
                    if (x, y, x2, y2) not in li:
                        li.append((x2, y2, x, y))
                        li.append((x, y, x2, y2))
                        count += 1
            elif i == 'D':
                x2, y2 = x, y - 1
                if y2 >= -5:
                    if (x, y, x2, y2) not in li:
                        li.append((x2, y2, x, y))
                        li.append((x, y, x2, y2))
                        count += 1
            x,y = x2,y2

        print(count)
        print(li)




test = test()
test.solution("ULURRDLLU")