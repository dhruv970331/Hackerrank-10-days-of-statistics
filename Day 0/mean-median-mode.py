# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
arr = [int(i) for i in input().split()]

# Mean
print(sum(arr)/n)
s = sorted(arr)

# Median
print((s[n//2]+s[(n//2)-1])/2)

counter = Counter(arr)
f = filter(lambda x: counter.get(x) >= max(counter.values()), counter.keys())
# Mode

print(min(f))
