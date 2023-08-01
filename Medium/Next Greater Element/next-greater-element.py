#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #logic is that we keep adding items to stacks then pop and check if the next elememnt is greater than it or not
        # logic is that we elements that remain at the top of the stack will always be smaller than the elements at the bottom
        stack =[]
        ans = [-1]*n
        for i in range(n):
            while stack:
                digit,pos = stack[-1]
                if arr[i] > digit:
                    stack.pop()
                    ans[pos] = arr[i]
                else:
                    stack.append([arr[i],i])
                    break
            else:
                stack.append([arr[i],i])
        return(ans)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends