import heapq


class test:
    def findKthLargest(self,arr, num):

        #print(arr,num)
        #print("작은수 정렬",arr(min(arr)))
        li =list()
        for i in arr:
            #print(i)
            heapq.heappush(li, i)


        print("fdasfdsafasd",heapq)
        print(li)
        print(type(li))
        for _ in range(1,num):
            heapq.heappop(li)
        print(heapq.heappop(li))


test = test()
test.findKthLargest([3,2,3,1,2,4,5,5,6], 4)

# assert test_maxheap([3,2,3,1,2,4,5,5,6], 1) ==6
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 2) ==5
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 3) ==5
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 4) ==4
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 5) ==3
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 6) ==3
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 7) ==2
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 8) ==2
# assert test_maxheap([3,2,3,1,2,4,5,5,6], 9) ==1
