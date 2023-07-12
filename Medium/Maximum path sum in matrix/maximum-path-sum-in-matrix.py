#User function Template for python3

class Solution:
    
    def maximumPath(self, n, matrix):
        for row in range (n-2,-1,-1):
            for col in range(n):
                if col == 0:
                    best = max (matrix[row+1][col],matrix[row+1][col+1])
                    matrix[row][col] += best
                elif col == n-1:
                    best = max (matrix[row+1][col],matrix[row+1][col-1])
                    matrix[row][col] += best
                else:
                    best = max (matrix[row+1][col],matrix[row+1][col-1],matrix[row+1][col+1])
                    matrix[row][col] += best
        ans = -1
        for col in range(n):
            ans = max (ans,matrix[0][col])
        return(ans)
            
            
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends