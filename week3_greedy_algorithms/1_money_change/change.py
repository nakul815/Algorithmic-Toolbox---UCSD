# Uses python3
import sys

def moneychange(m):
    coins=0
    while (m>=10):
        coins=coins+1
        m=m-10
    while (m>=5):
        coins=coins+1
        m=m-5
    return coins+m

# Test 
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(moneychange(m))
