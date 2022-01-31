import sys

num = int(sys.stdin.readline())
print(num)

move = sys.stdin.readline()
replaceMove = move.replace(" ", "")
print(replaceMove)

x, y = 1, 1

for i in range(0, len(replaceMove) - 1):
    #print(replaceMove[i])
        if replaceMove[i] == 'L':
            if y > 1:
                x, y = x, y -1

        elif replaceMove[i] == 'R':
            if y < 5:
                x, y = x, y + 1
                print(x, y)

        elif replaceMove[i] == 'U':
            if x > 1:
                x, y = x - 1, y

        elif replaceMove[i] == 'D':
            if x < 5:
                x, y = x + 1, y

print(x, y)