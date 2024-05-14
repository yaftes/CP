s = "erase*****"
stack = []
for e in s:
    if stack and e == '*':
        stack.pop()
    else:
        stack.append(e)
print("".join(stack))