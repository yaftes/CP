# there are 3 colored stones red,green and blue
# count minimum number of stones to take from the table
# so that any two neighbouring stones had different colors
# in the other sense finding the longest substring which has diffennt colors of neighbours
# we could use sliding window technique
n = int(input())
s = input()
count = 0
left,right = 0,0
while left <= right and right < n-1:
    if s[right] != s[right+1]:
        right+=1
    else:
        right+=1
        left=right
        
    count = max(count,right-left+1)
print(n-count)
    