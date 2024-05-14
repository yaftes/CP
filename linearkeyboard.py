t = int(input())
fvalue = []
for v in range(t):
    order = input()
    target = input()
    alph_ord = {}
    value = 0
    for i in range(0,len(order)):
        alph_ord[order[i]] = i+1
    for j in range(len(target)-1):
        value += abs(alph_ord[target[j]] - alph_ord[target[j+1]])
    
    fvalue.append(value)
for a in fvalue:
    print(a)
