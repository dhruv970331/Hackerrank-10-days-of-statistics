# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
arr = [int(i) for i in input().split()]

# print(arr)

# Mean
print(sum(arr)/n)
s = sorted(arr)

#Median
print((s[n//2]+s[(n//2)-1])/2)

counter = Counter(arr)
# f = filter(lambda x,y:x if y==min(counter.values()),counter.items())
# Mode
print(min(counter))