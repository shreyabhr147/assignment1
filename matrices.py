l1=[[1,2],[3,4]]
l2=[[5,6],[7,8]]
mul=[[0,0],[0,0]]
for i in range(len(l1)):
    for j in range(len(l2[0])):
        for k in range(len(l1)):
            mul[i][j]=mul[i][j]+l1[i][k]*l2[k][j]
            

for i in mul:
    print(i)
