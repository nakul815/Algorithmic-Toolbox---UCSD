# Uses python3

# Input n, generate Fn

def fibonacci(n):
    arr=[0]*(n+1)
    if n==0:
        return n
    
    arr[0]=0
    arr[1]=1
    for i in range(2,n+1):
        arr[i]=arr[i-1]+arr[i-2]
    #return [arr[0:n+1],arr[n]]    
    return arr[n]
    
# Test Fibonacci Number Generation (Naive Solution)
if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci(input_n))  
