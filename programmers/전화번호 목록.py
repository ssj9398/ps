class cellNumber:
    def solution(self,phone_book):

        for i in range(len(phone_book)):
            print(i)
            if i !=0:
                find = phone_book[i].find(phone_book[0])
                print("res",find)
                if find == 0:
                    print("False")
        print(phone_book)

cellNumber = cellNumber()
cellNumber.solution(["123","456","789"])