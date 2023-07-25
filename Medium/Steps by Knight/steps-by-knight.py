class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, n):
        #n ,n2 =8,8
        
        queue =[]
        visited = [[0 for i in range(n)] for j in range (n)]
        k1,k2 = KnightPos
        queue.append([k1-1,k2-1])
        steps = 0
        count =1
        while queue:
            k = len(queue)
            steps +=1
            for i in range (k):
                i,j = queue.pop(0)
                if [i+1,j+1]== TargetPos:
                    return(steps-1)
     
                
                
                if i+2 < n and j+1 <n: # case1
                    if visited[i+2][j+1] == 0 :
                        visited[i+2][j+1] =1
                        queue.append([i+2,j+1])
                
                if i+2 < n and j-1 >=0: # case2
                    if visited[i+2][j-1] == 0 :
                        visited[i+2][j-1] = 1
                        queue.append([i+2,j-1])
                        
                if i+1 < n and j+2 <n: 
                    if visited[i+1][j+2] == 0 :
                        visited[i+1][j+2] =1
                        queue.append([i+1,j+2])
                        
                if i+1 < n and j-2 >=0: # case4
                    if visited[i+1][j-2] == 0 :
                        visited[i+1][j-2] =1
                        queue.append([i+1,j-2])
                        
                if i-2 >=0 and j+1 <n: # case1
                    if visited[i-2][j+1] == 0 :
                        visited[i-2][j+1] =1
                        queue.append([i-2,j+1])
                
                if i-2 >=0 and j-1 >=0: # case2
                    if visited[i-2][j-1] == 0 :
                        visited[i-2][j-1] =1
                        queue.append([i-2,j-1])
                        
                if i-1 >=0 and j+2 <n: # case3
                    if visited[i-1][j+2] == 0 :
                        visited[i-1][j+2] =1
                        queue.append([i-1,j+2])
                        
                if i-1 >=0 and j-2 >=0: # case4
                    if visited[i-1][j-2] == 0 :
                        visited[i-1][j-2] =1
                        queue.append([i-1,j-2])
            #count =0
            #steps +=1
  
        return(-1)    
      

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends