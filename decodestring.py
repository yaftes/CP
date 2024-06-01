"""
given a string 
s = "2[a]3[b]" ---- > aabbb
s = 2[a3[c]]bc ---- > acccacccbc
s = ksjglkjal

"""
# for no nested square bracket
s = "2[a2[c]]3[b]"
stack = []
curr =  ""
final = ""
for i in range(len(s)):
    if s[i].isdigit():
        stack.append(int(s[i]))
    elif s[i] == "]" and stack:
        final += curr * stack.pop()
        curr = ""
    elif s[i] == "[":
        final += curr
        curr = ""
    else:
        curr+=s[i]
final += curr
print(final)
    