#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        sol =[[0 for i in range(y+1)] for j in range(x+1) ] 
        for row in range(1,x+1):
            for col in range(1,y+1):
                if s1[row-1] == s2[col-1]:
                    sol[row][col]=1+sol[row-1][col-1]
                else:
                    sol[row][col]=max(sol[row-1][col],sol[row][col-1])
        #print(sol)
        return(sol[x][y])
        
        # code here


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
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends