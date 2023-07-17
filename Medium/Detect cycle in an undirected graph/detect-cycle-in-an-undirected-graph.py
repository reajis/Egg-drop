from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    #print(adj)
        visited = set()
        stack =[]
        for i in range (V):
            if i not in visited:
                #print("i",i)
                stack.append(i)
            while stack:
                current_node = stack.pop()
                if current_node in visited:
                    #print("problematic node is ",current_node )
                    return(True)
                else:
                    #print("2",current_node)
                    visited.add(current_node)
                for node in adj[current_node]:
                    if node not in visited:
                        #print("3",node)
                        stack.append(node)
                    
        return(False)


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends