count = 0
tickets = [84,49,5,24,70,77,87,8]
k = 3
while tickets[k] > 0:
    for i in range(len(tickets)):
        if tickets[i] > 0:
            count +=1
            tickets[i]-=1
        if tickets[i] == 0:
            break
print(count)