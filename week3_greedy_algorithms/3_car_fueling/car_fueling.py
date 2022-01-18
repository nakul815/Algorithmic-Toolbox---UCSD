# python3
import sys

def MinRefills(x,n,L):
    numRefills=0
    currentRefill=0
    while (currentRefill<=n):
        lastRefill = currentRefill
        while (currentRefill<=n and x[currentRefill+1]-x[lastRefill]<=L):
            currentRefill=currentRefill+1
            if currentRefill==lastRefill:
                return IMPOSSIBLE
            if currentRefill<=n:
                numRefills=numRefills+1
        return numRefills

# Test 
if __name__ == '__main__':
    input_a = int(input())
    input_L = int(input())
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(MinRefills(input_numbers,input_n,input_L))

#if __name__ == '__main__':
#    d, m, _, *input_numbers = map(int, sys.stdin.read().split())
#    print(compute_min_refills(d, m, stops))
#     print(MinRefills(input_numbers,input_n,input_L))	
