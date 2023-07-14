#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        ans = []
        queue =[]
        visited = set()
        visited.add(0)
        queue.append(0)
        #for i in range(V):
        #i = 0
        while queue:
            current_node = queue.pop(0)
            ans.append(current_node)
            #if current_node not in visited:
                #ans.append(current_node)
                #visited.add(current_node)
            if adj[current_node]:    
                for node in adj[current_node]:
                    if node not in visited:
                        queue.append(node)
                        visited.add(node)
          

        return(ans)


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends