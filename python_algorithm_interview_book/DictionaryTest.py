score_dict = {
    'sam':23,
    'john':30,
    'mathew':29,
    'riti':27,
    'aadi':31,
    'sachin':28
}

temp_dict = {}

# for i in score_dict:
#     if score_dict.get(i)>28:
#         temp_dict[i] = score_dict.get(i)

temp_dict = dict(filter(lambda elem:elem,score_dict.items()))

dict = list(temp_dict)
print(temp_dict)
print(dict)


a = [1,2,3]
b = [6,7,8]

c = {k:v for k,v in zip(a,b)}
print(c)
d = {k:v for k,v in enumerate(a,b)}
e = {k:v for k,v in zip(range(len(b)),b)}
print(c)
print(d)
print(e)


a = [1, 2, 3]
b = [6, 7, 8]
c = {k:v for k, v in zip(a,b)}
d = {k:v for k, v in enumerate(b)}
e = {k:v for k, v in zip(range(len(b)), b)}
print(c)
print(d)
print(e)