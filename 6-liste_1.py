lst=[[1,2],[3,4],[5,6],[7,8],[9,10]]
for i1 in lst:
    for i2 in i1:
        print(i2)

for i1 in range(0,len(lst)):
    for i2 in range(0,len(lst[i1])):
        print(lst[i1][i2])