#User function Template for python3

class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        if n == 0 or n == 1 :
            return(1)
        ans = 1
        for i in range (1 ,n):
            ans = (2*(2*i+1)*ans)//(i+2)
        return(ans)
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends