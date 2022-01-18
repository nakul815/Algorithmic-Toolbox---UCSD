# Uses python3
import sys

def primitive_calc(n):
    import sys
    table = [0 for i in range(n)] 
    min_oper = [0 for i in range(n)] 
  
    # Base case 
    table[0] = 1
    min_oper[0]=0   
    
    # Compute minimum coins required  
    # for all values from 1 to money    
    temp_3=temp_2=temp_1=sys.maxsize    
    for i in range(1, n):    
        if (i+1) % 3==0: 
            temp_3=min_oper[(i//3)]+1
    
        if (i+1) % 2==0: 
            temp_2=min_oper[(i//2)]+1
    
        temp_1=min_oper[i-1]+1
    
        min_oper[i]=min(temp_3,temp_2,temp_1)
        
        if min(temp_3,temp_2,temp_1)==temp_1: 
            table[i]=1
        if min(temp_3,temp_2,temp_1)==temp_2: 
            table[i]=2
        if min(temp_3,temp_2,temp_1)==temp_3: 
            table[i]=3
        
        temp_3=temp_2=temp_1=sys.maxsize
    
    j=n
    numbers=[]
    while (j>1):
        if table[j-1]==1:
            numbers.append(j-1)
            j=j-1
        if table[j-1]==2:
            numbers.append(j//2)
            j=j//2
        if table[j-1]==3:
            numbers.append(j//3)
            j=j//3    
    numbers.reverse()
    numbers.append(n)
    min_oper=min_oper[n-1]
    return min_oper, numbers

# Driver Code 
if __name__ == "__main__": 
  
    #coins = [9, 4, 2] 
    #coins = [int(x) for x in input().split()]
    #n = 12
    n = int(input())
    sequence = list(primitive_calc(n))
    print(sequence[0])
    sequence=sequence[1]
    for x in sequence:
        print(x, end=' ')
