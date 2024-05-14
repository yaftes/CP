temp= [73,74,75,71,69,72,76,73]
hm = {}
for i in range(len(temp)):
    hm[i] = temp[i]
stack = []
res = [0] * len(temp)
for i in range(len(temp)):
    while stack and hm[stack[-1]] < temp[i]:
        res[stack[-1]] = abs(i-stack[-1])
        stack.pop()
    stack.append(i)
print(res)