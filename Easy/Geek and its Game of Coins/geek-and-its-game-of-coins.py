#User function Template for python3
class Solution:

	def findWinner(self, n,x,y):
	    b = max (x,y)
	    a = min(x,y)
		arr = [False,True]

		for i in range (2,n+1):
		    if a>i:
		        index1 = i-1
		        arr.append(not arr[index1])
		    elif i>=a and b>i:
		        index1 = i-1
		        index2 = i-a
		        ans = (not arr[index1] or not arr[index2])
		        arr.append(ans)
		    else:
		        index1 = i-1
		        index2 = i-a
		        index3 = i-b
		        ans = (not arr[index1] or not arr[index2] or not arr[index3])
		        arr.append(ans)
		        
		  
		       
		   
		if arr[n] == True :
		    return 1
		else :
		    return 0
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,X,Y = input().split()
		N,X,Y = int(N),int(X),int(Y)
		ob = Solution()
		ans = ob.findWinner(N,X,Y)
		print(ans)

# } Driver Code Ends