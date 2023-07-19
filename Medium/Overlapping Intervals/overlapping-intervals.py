class Solution:
	def overlappedInterval(self, intervals):
	    result =[]
	    intervals.sort(key = lambda x:x[0])
	    #print(intervals)
	    i =0
	    while i < len(intervals)-1:
	        if intervals[i][1] >= intervals[i+1][0] and intervals[i][1] >= intervals[i+1][1]:
	            #print("case1 ",i+1)
	            intervals.pop(i+1)
	            #print(intervals)
	            # no need to increment i
	        elif intervals[i][1] >= intervals[i+1][0] and intervals[i+1][1] >= intervals[i][1]:
	            #print("case2 ",i+1)
	            intervals[i][1] = intervals[i+1][1]
	            intervals.pop(i+1)
	            #print(intervals)
	        else :
	            #print("case ",i+1)
	            i +=1
	            
	    return(intervals)
	           
	       
	       
	        
	        
		return(Intervals)


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends