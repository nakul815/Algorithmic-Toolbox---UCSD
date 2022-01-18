#Uses python3
import sys
import math

def closestpoint(P,Q,n):
    if n <= 3:  
        return closestpoint_brute(P,n)
    # Find the middle point
    mid=n//2
    midpoint=P[mid]
    dl=closestpoint(P[:mid],Q,mid)
    dr=closestpoint(P[mid:], Q, n - mid)  
    # Find the smaller of two distances  
    d = min(dl, dr)
    
    # Build an array strip[] that contains points close (closer than d)  
    # to the line passing through the middle point  
    strip = []  
    for i in range(n):  
        if abs(Q[i][0] - midpoint[0]) < d:  
            strip.append(Q[i]) 
    # Find the closest points in strip. Return the minimum of d and closest  
    # distance is strip[]  
    return min(d, stripClosest(strip, len(strip), d)) 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    P = data[1::2]
    Q = data[2::2]
    print("{0:.9f}".format(closestpoint(P,Q,n)))
