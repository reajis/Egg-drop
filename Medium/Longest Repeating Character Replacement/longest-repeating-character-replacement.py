#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
    
        count = {}
        l = 0
        high = 0
        
        for r in range(len(s)):
            
            count[s[r]] = count.get(s[r],0) +1
          
            length = r - l + 1
            if length - max(count.values()) <= k:
                high = max(high, length)
            else:
                count[S[l]] -= 1
                l += 1
                
        return high
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends