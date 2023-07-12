#User function Template for python3

class Solution:
	def nthStair(self,n):
        steps =[1,2]
        arr = [[0 for cols in range(n+1)] for rows in range (len(steps))]
        for j in range (1,n+1):
                arr[0][j] = 1 
        i = 1
        for j in range(n+1):
            if j < steps[i]:
                arr[i][j] = arr[i-1][j]
            else:
                if j == steps[i] :
                    arr[i][j] = arr[i-1][j] +1
                else :
                    arr[i][j] = arr[i-1][j] +arr[i][j-steps[i]]
        return(arr[1][n])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)
# } Driver Code Ends