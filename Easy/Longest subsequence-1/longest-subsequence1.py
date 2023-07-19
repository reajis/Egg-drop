#User function Template for python3

class Solution:
    def longestSubsequence(self, n, arr):
        num = [1 for i in range (n)]
        best = 1
        for i in range (n):
            for j in range (i):
                if abs(arr[j]-arr[i])== 1:
                    num[i] = max (num[i],1+num[j])
                    best = max(best,num[i])
        return(best)
                    
                    
                
     


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for itr in range(N):
            A[itr] = int(A[itr])
        
        ob = Solution()
        print(ob.longestSubsequence(N, A))
# } Driver Code Ends