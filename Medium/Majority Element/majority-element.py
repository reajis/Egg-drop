#User function template for Python 3

class Solution:
    def majorityElement(self, arr,n):
        dicti =  {}
        ans =0
        ele =-1
        for i in range (n):
            dicti[arr[i]] = dicti.get(arr[i],0)+1
            if dicti[arr[i]] > ans:
                ans =dicti[arr[i]]
                ele = arr[i]
        if ans >n//2:
            return(ele)
        
        return(-1)
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends