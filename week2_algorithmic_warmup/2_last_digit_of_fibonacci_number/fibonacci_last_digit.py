# Python3
import sys

# Input n, generate last Digit Fn

def fibonacci_last(n):
    arr=[0]*(n+1)
    if n==0:
        return n
    
    arr[0]=0
    arr[1]=1
    for i in range(2,n+1):
        arr[i]=(arr[i-1]+arr[i-2])%10
    return arr[n]   

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_last(n))
