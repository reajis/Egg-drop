#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        i = len(S)-1
        j= len(S)-2
        
        while j>=0:
            if S[i]==S[j]:
                S = S[:i] +S[i+1:]
            i = i-1
            j = j-1
        #print
        return(S)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends