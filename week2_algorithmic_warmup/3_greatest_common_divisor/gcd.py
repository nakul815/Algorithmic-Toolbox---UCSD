# Uses python3
import sys

#Reduce Find GCD of a,b . Input a,b>=0 , Output gcd(a,b)

# Euclid Property: GCD(a,b)=GCD(b,a') where a' is remainder after diving a with b

def gcd(a,b):
    if a==0 or b==0:
        return max(a,b)
    
    a1=a%b
    return gcd(b,a1)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
