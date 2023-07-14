#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = set()
        stack = []
        ans = []
        #visited.add(0) # ??
        stack.append(0)
        #print(adj)
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                ans.append(current_node)
            n = len(adj[current_node])
            for i in range(n-1,-1,-1):
                node = adj[current_node][i]
                if node not in visited:
                    #print(node)
                    stack.append(node)
                    
            #print("break")
        return(ans)    
   


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends