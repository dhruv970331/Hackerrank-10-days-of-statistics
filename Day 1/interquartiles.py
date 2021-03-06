# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import repeat
from functools import reduce

def median(arr):
    n = len(arr)
    if n%2==0:
        return sum(arr[(n//2)-1:(n//2)+1])/2
    return float(arr[n//2])

n = int(input())

X = list(map(int,input().split()))
F = list(map(int,input().split()))
S = [list(repeat(x,f)) for x,f in zip(X,F)]
S =  sorted(reduce(lambda a,b:a+b,S))
# print(S)

N = len(S)

q1 = median(S[:N//2])
q3 = median(S[N//2:]) if n%2==0 else median(S[N//2+1:])

print(round(q3-q1,1))