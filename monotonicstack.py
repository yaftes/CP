
arr = [4,5,2,3]

hm = {}
stack = []
for i in range(len(arr)):
    while stack and arr[i] > stack[-1]:
        hm[stack.pop()] = arr[i]
    if len(stack) == 0 or arr[i] < stack[-1]:
        stack.append(arr[i])
print(stack)
print(hm)



