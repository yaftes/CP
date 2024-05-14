l = int(input())
m = input()
def genome(n,s):
    if n % 4 != 0:
        return "==="
    hm = {'A':0,'C':0,'T':0,'G':0,'?':0}
    for i in range(n):
        hm[s[i]] += 1
        if hm[s[i]] > n//4 and s[i] != '?':
            return "==="
    bucket = {'A','C','T','G'}
    fa = ""
    for j in range(n):
        if s[j] != '?':
            fa+=s[j]
        else:
            for char in bucket:
                if hm[char] < n//4:
                    fa += char
                    hm[char] +=1
                    break
    return fa
print(genome(l,m)) 
# type of errors i got on solving this problem KeyError,......