class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		rows = len(grid)
		cols =len(grid[0])
		stack = []
		ones =0
		for row in range (rows):
		    for col in range(cols):
		        if grid[row][col] ==2:
		            #print("here",row,col)
		            stack.append([row,col])
		        elif grid[row][col] ==1:
		            ones +=1
		step =0
		changed =0
		while stack:
		    
		    n = len(stack)
		    count =0
		    for i in range(n):
		        row,col=stack.pop(0)
		        #print(n,row,col)
		        #case1 up
		        
		        if row-1>=0:
		            if grid[row-1][col]==1:
		                count+=1
		                grid[row-1][col]= 2
		                changed +=1
		                stack.append([row-1,col])
		        #case2 down
		        if row+1<rows:
		            if grid[row+1][col]==1:
		                count+=1
		                grid[row+1][col]= 2
		                changed +=1
		                stack.append([row+1,col])
		        #case3 left
		        if col-1>=0:
		            if grid[row][col-1]==1:
		                count+=1
		                grid[row][col-1]= 2
		                changed +=1
		                stack.append([row,col-1])
		        #case4 right
		        if col+1<cols:
		            if grid[row][col+1]==1:
		                count+=1
		                grid[row][col+1]= 2
		                changed +=1
		                stack.append([row,col+1])
		        
		           
		    if count !=0:
		        step +=1
        if changed !=ones:
            return(-1)
		return(step)
		


#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends