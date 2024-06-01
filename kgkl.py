logs = ["./","../","./"]
stack = []
for i in range(len(logs)):
    if stack and logs[i] == "../":
        stack.pop()
    elif logs[i] == "./" or logs[i] == "../":
        continue
    else:
        stack.append(logs[i])
print(stack)