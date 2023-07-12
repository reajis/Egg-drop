#User function Template for python3
class Solution:
	def maxSubstring(self, S):

	    ones=[]
	    zeroes =[]
	    for ch in S:
	        if ch =='1':
	            ones.append(1)
	            zeroes.append(0)
	        else:
	            ones.append(0)
	            zeroes.append(1)
        n = len(zeroes)
	    maxi = zeroes[n-1]- ones[n-1]
	    for i in range (n-2,-1,-1):

            option1 = ( (zeroes[i+1]+zeroes[i])-(ones[i+1]-ones[i]) )>(zeroes[i]-ones[i])
            if option1:
                ones[i]= ones[i]+ones[i+1]
                zeroes[i]= zeroes[i]+zeroes[i+1]
            maxi = max (maxi,zeroes[i]-ones[i])
        return(maxi)
	            
	        
	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends