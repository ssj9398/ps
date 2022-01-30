class test:
    def largest_number(self,arr):

        for i in range(1,len(arr)):
            for j in range(1,len(arr)):
                print(i,j)
                if str(arr[j-1]) + str(arr[j]) < str(arr[j]) + str(arr[j-1]):
                    arr[j], arr[j-1] = arr[j-1],arr[j]
        print(arr)
        print(''.join(map(str, arr)))


test = test()
test.largest_number([3,30,34,5,9])