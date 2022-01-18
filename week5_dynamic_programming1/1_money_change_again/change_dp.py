# Uses python3
import sys
def minCoins(coins, money): 
    m = len(coins)   # m is size of coins array (number of different coins)
    # table[i] will be storing the minimum number of coins required for i value.  
    table = [0 for i in range(money + 1)] 
  
    # Base case 
    table[0] = 0
  
    # Initialize all table values as Infinite 
    for i in range(1, money + 1): 
        table[i] = sys.maxsize 
  
    # Compute minimum coins required  
    # for all values from 1 to money 
    for i in range(1, money + 1): 
          
        # Go through all coins smaller than i 
        for j in range(m): 
            if (coins[j] <= i): 
                MinNumCoins = table[i - coins[j]] #Check min coins required for 'i - coins[j]' 
                if (MinNumCoins != sys.maxsize and #Checks if coins for i - coins[j]' were feasible
                    MinNumCoins + 1 < table[i]): #Checks if this is minimum
                    table[i] = MinNumCoins + 1
    return table[money]

# Driver Code 
if __name__ == "__main__": 
  
    coins = [1, 3, 4] 
    #coins = [int(x) for x in input().split()]
    #V = 12
    V = int(sys.stdin.read())
    print(minCoins(coins, V))

