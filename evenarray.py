#merge two sorted array

# for num1 swap 
# for num2 change


mapping = {'0':'0000','1':'0001','2':'0010','3':'0011','4' : '0100','5' : '0101','6' : '0110','7' : '0111','8' : '1000','9' : '1001','A' : '1010','B' : '1011','C':'1100','D' : '1101','E' : '1110','F' : '1111'}
def Calculate(a,b):
    c = mapping[a] + mapping[b]
    j = 0
    tot = 0
    for i in range(len(c)-1,-1,-1):
        tot += int(c[i])*(2**j)
        j+=1
    return chr(tot)
print(Calculate('3',''))









