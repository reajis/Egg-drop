#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        start = {"{","(","["}
        closed = {"}",")","]"}
        stack =[]
        for ele in x :
            #print(ele)
            if ele in start:
                #print("1",ele)
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return(False)
                if ele =="}":
                    if stack[-1] == "{":
                        #print("2",ele)
                        stack.pop()
                    else:
                        #print("3",ele)
                        return False
                elif ele==")":
                    if stack[-1] == "(":
                        #print("4",ele)
                        stack.pop()
                    else:
                        #print("5",ele)
                        return False
                
                else:
                    if stack[-1] == "[":
                        #print("6",ele)
                        stack.pop()
                    else:
                        #print("7",ele)
                        return False
        if len(stack)==0:
            return(True)
        else:
            return(False)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


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
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends