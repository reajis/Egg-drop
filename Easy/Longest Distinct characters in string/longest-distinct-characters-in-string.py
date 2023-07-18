#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, s):
        n = len(s)
        if n ==1 or n == 0:
            return(n)
        best =1
        i =0
        j=0
        dicti =[]
        while j<n:
            if s[j] in dicti :
                dicti.pop(0)
                i+=1
            else :
                dicti.append(s[j])
                length = j-i+1
                best = max(length,best) 
                j+=1
                
        return(best)

            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends