# 무지의 먹방 라이브
# 배열 li가 있고 i는 0부터 시작해 -1씩 차감하며 마지막 i에 도달했을때 다시 0으로 돌아오게 된다.

class test:
    def muzi(self,food_times, k):
        count = 0
        print(food_times, k)
        while True:
            for i in range(len(food_times)):
                # print(food_times[i])
                if food_times[i] !=0:
                    food_times[i] -= 1
                    #print(food_times[i])
                    print(food_times)
                    count+=1
                    print("count",count)
                    print("i+1번째 음식 = ",i)
                    if count+1==k:
                        print("k번째일때 먹어야 할 음식 = ",i+1)
                        break
                #print(i+1)
                # if food_times[i]==0:
                #     print("끝")
                #     break

test = test()
test.muzi([3,1,2],5)