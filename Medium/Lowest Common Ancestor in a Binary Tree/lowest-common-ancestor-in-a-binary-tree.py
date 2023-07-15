#User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:

    def ifNodeExists(self,node, key):
     
        if (node == None):
            return False
     
        if (node.data == key):
            return True
     
    
        res1 =self.ifNodeExists(node.left, key)
        # node found, no need to look further
        if res1:
            return True
    
        res2 = self.ifNodeExists(node.right, key)
     
        return res2
    
    def isparent(self,root, n1, n2):
        condition1 = self.ifNodeExists(root, n1)
        condition2 = self.ifNodeExists(root, n2)
        return(condition1 and condition2)
        
        
    
    def lca(self,root, n1, n2):
        condition = True

        current_node = root 
        while current_node:
            
            if current_node.left and self.isparent(current_node.left, n1, n2):
                current_node =current_node.left
            elif current_node.right and self.isparent(current_node.right, n1, n2):
                current_node =current_node.right
            else:
                break
            
        
        return(current_node)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        a,b=list(map(int,input().split()))
        s=input()
        root=buildTree(s)
        k=Solution().lca(root,a,b)
        print(k.data)



# } Driver Code Ends