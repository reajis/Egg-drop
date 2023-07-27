#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        queue =[]
        rows = len(grid)
        cols = len(grid[0])
        #print(rows,cols)
        visited = [[0 for i in range(cols)] for j in range (rows)]
        
        count = 0
        for row in range (rows):
            for col in range(cols):
                #print("#",row,col)
                if visited[row][col] ==0 and grid[row][col] == 1:
                    visited[row][col] = 1
                    queue.append([row,col])
                    #print(row,col)
                    count+=1
                    while queue:
                        
                        i,j = queue.pop(0)
                        #print(i,j)
                        
                        if i+1 < rows and j+1 <cols: # case1
                            if visited[i+1][j+1] == 0 and grid[i+1][j+1] ==1:
                                visited[i+1][j+1] =1
                                queue.append([i+1,j+1])
                        
                        if i+1 < rows and j-1 >=0:
                            if visited[i+1][j-1] == 0 and grid[i+1][j-1] ==1 :
                                visited[i+1][j-1] = 1
                                queue.append([i+1,j-1])
                                
                        if i+1 < rows: 
                            if visited[i+1][j] == 0 and grid[i+1][j] ==1:
                                visited[i+1][j] =1
                                queue.append([i+1,j])
                                
                        if j-1 >=0: # case4
                            if visited[i][j-1] == 0 and grid[i][j-1] ==1 :
                                visited[i][j-1] =1
                                queue.append([i,j-1])
                                
                        if i-1 >=0 : # case1
                            if visited[i-1][j] == 0 and grid[i-1][j]  ==1 :
                                visited[i-1][j] =1
                                queue.append([i-1,j])
                        
                        if i- 1>=0 and j-1 >=0: # case2
                            if visited[i-1][j-1] == 0 and grid[i-1][j-1]  ==1 :
                                visited[i-1][j-1] =1
                                queue.append([i-1,j-1])
                                
                        if i-1 >=0 and j+1 <cols: # case3
                            if visited[i-1][j+1] == 0 and grid[i-1][j+1]==1 :
                                visited[i-1][j+1] =1
                                queue.append([i-1,j+1])
                                
                        if  j+1 <cols: # case4
                            if visited[i][j+1] == 0 and grid[i][j+1]==1 :
                                visited[i][j+1] =1
                                queue.append([i,j+1])
        #print(visited)
        return(count)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends