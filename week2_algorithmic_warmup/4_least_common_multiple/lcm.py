# Python3
import sys

#Note that GCD*LCM= a*b

def gcd(a,b):
    if a==0 or b==0:
        return max(a,b)
    
    a1=a%b
    return gcd(b,a1)

def lcm(a,b):
    if a==0 and b==0:
        return 0
    
    return a*b/gcd(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(int(lcm(a, b)))

