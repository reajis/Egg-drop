#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, s):
        count = {}
        l = 0
        high = 0
        r =0
        prev_right =-1
        while r < len(s):
            if r != prev_right:
                count[s[r]] = count.get(s[r],0) +1
                prev_right =r
          
            length = r - l + 1
            if count[s[r]] <= 1:
                #print("1",s[r])
                high = max(high, length)
                r +=1
            else:
                #print("2",s[r])
                count[s[l]] -= 1
                l += 1
            #print("high",high)
                
        return high

            
            
            


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