#User function Template for python3

class Solution:
    def count(self, coins, n, Sum):
        coins.sort()
        result = [[0 for i in range(Sum+1)] for j in range(n)]
        result[0][0] = 1
        for value in range (1,Sum+1):
            if value >= coins[0] and value %coins[0] ==0 :
                result[0][value] =1
                                  
                
        for j in range(1,n):
            for i in range(0,Sum+1):
                if i == 0:
                    result[j][i] = 1
                    continue
                if i< coins[j]:
                    #print(i,coins[j])
                    result[j][i] = result[j-1][i]
                else:
                    #print(i,coins[j])
                    result[j][i] = result[j-1][i] + result[j][i-coins[j]]
                
            
        #print(result)
        return(result[n-1][Sum])
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends