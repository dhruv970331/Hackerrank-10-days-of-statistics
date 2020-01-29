# Enter your code here. Read input from STDIN. Print output to STDOUT

def median(arr):
    middle = len(arr)//2
    if len(arr)%2 == 0:
        return sum(arr[middle-1:middle+1])//2
    return arr[middle]

n = int(input())
arr = sorted(list(map(int,input().split())))

q1 = median(arr[:n//2])
q2 = median(arr)
q3 = median(arr[n//2:]) if n%2==0 else median(arr[n//2+1:])
print(q1)
print(q2)
print(q3)