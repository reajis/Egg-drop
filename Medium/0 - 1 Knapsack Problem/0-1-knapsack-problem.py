#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        

class Solution:
    def knapSack(self,W, wt, val, n):
        arr = []
        for i in range (n):
            item= Item(val[i],wt[i])
            arr.append(item)
         
        result = [[0 for cols in range(W+1)] for rows in range(n)]
        arr.sort(key = lambda x:x.weight)
       # print(result)

        
        for value in range (W+1):
            if value >=arr[0].weight:
                result [0][value] = arr[0].value
        #print(result)
        
        for j in range (1,n):
            for value in range(W+1):
                if arr[j].weight > value:
                    #print(1)
                    result[j][value] =result[j-1][value]
                else :
                    #print(2)
                    result[j][value] =max(result[j-1][value],arr[j].value+result[j-1][value-arr[j].weight])
            #result[0] = result[j]
    
                
        #print(result)
        
        return(result[n-1][W])
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends