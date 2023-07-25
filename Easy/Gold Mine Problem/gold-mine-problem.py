# User function Template for Python3

class Solution:
    def maxGold(self, n, m, mine):
        ans = 0
        if m ==1:
            for i in range (n):
                ans = max (mine[i][0],ans)
            return(ans)
        elif n ==1:
            for i in range (m):
                ans +=mine[0][i]
            return(ans)
        #create empty array
        # start to fill array from the last row 
        #print(mine)
        
        for col in range (m-2,-1,-1):
            for row in range (n):
                #print(row,col)
                #case1
                if row == 0:
                    add = max (mine[row][col+1],mine[row+1][col+1])
                elif row == n-1:
                    add = max (mine[row][col+1],mine[row-1][col+1])
                else:
                    add = max (mine[row][col+1],mine[row-1][col+1],mine[row+1][col+1])
                mine[row][col]= add + mine[row][col]
                #print(mine[row][col])
                ans = max (ans,mine[row][col])
        #print(mine)
        return(ans)
                    


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends