# for loop decides for how many iterations should something be perfomed

x,y,z,n = 1,1,2,3
ans = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if sum([i,j,k]) != n:
                ans.append([i,j,k])
print(ans)