class test:
    def solution(self,phone_number):
        len_num = len(phone_number)-4
        reverse = phone_number[::-1][0:4]
        to_rev = reverse[::-1]
        print("*"*len_num+to_rev)


test = test()
test.solution("027778888")