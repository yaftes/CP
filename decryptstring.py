s = "10#11#12"
alphabet_mapping = {}
for i in range(1, 27):
    if i > 9:
        alphabet_mapping[str(i)+"#"] = chr(ord('a') + i - 1)
    else:
        alphabet_mapping[str(i)] = chr(ord('a') + i - 1)
#reverse tracking
n = len(s)-1
ans = ""
while n  > -1:
    if s[n] != "#":
        ans += alphabet_mapping[s[n]]
        n-=1
    else:
        ans += alphabet_mapping[s[n-2:n+1]]
        n-=3
print(ans[::-1])

