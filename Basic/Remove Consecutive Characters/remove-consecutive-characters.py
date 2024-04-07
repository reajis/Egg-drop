#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        new_string = ""
        for i in S:
            if new_string == "":
                new_string += i
            elif new_string[-1] != i:
                new_string += i
        return(new_string )
                
            
                
        # code here


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