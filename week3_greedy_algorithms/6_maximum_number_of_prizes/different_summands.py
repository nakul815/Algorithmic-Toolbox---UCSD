# Uses python3
import sys

# Max number of prizes

#Find max k such that n=a1+..ak are positive distint integers
#Eg: Input 7 then Output is 3 and 1 2 4 i.e1+2+4


def maxprizes(n):
    k=0
    for i in range(1,n):
        if (i*(i+1)/2 < n and (i+1)*(i+2)/2 >= n):
            k=i
            break
        i=i+1
    a=[i for i in range(1,k)]
    if n-sum(a)>0:
        a.append(n-sum(a))
    print(k)
    print(' '.join([str(i) for i in a]))

# Test 
if __name__ == '__main__':
    input_n = int(input())
    (maxprizes(input_n))
