# Uses python3
import sys
import math

def BinarySearch(A, low, high, key): 
    if high<low: return 0
    
    mid= math.floor (low +(high-low)/2)
    
    if key==A[mid]:
        return mid+1
    
    elif key<A[mid]:
        return BinarySearch(A, low, mid -1, key)

    elif key>A[mid]:
        return BinarySearch(A, mid+1, high, key)
    else: return 0


import sys
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    A = data[1 : n + 1]
    for key in data[n + 2:]:
        low, high = 0, n-1
        print(BinarySearch(A, low, high, key)-1, end = ' ')
