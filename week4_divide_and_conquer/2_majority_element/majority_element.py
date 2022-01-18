# Uses python3
import sys

def GetMajortiyElement(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    half = len(a) // 2
    left = GetMajortiyElement(a[0:half])
    right = GetMajortiyElement(a[half:])
    if left == right:
        return left
    if a.count(left) > half:
        return left
    if a.count(right) > half:
        return right
    return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if GetMajortiyElement(a) != -1:
        print(1)
    else:
        print(0)
