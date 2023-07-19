#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        x = len(s)
        sol =[[0 for i in range(x+1)] for j in range(x+1) ] 
        for row in range(1,x+1):
            for col in range(1,x+1):
                #backwardindex = -col
                if s[row-1] == s[-col]:
                    sol[row][col]=1+sol[row-1][col-1]
                else:
                    sol[row][col]=max(sol[row-1][col],sol[row][col-1])
        #print(sol)
        return(sol[x][x])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends