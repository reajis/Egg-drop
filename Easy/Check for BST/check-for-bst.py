#User function Template for python3


class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def remove_nones(self,items):
        return[x for x in items if x is not None]
        
    def bst_check(self,node):
        if node == None:
            return (True , None , None)
        
        left_bst , left_min, left_max = self.bst_check(node.left)
        right_bst , right_min, right_max = self.bst_check(node.right)
        
        bst = (left_bst and right_bst) and ((left_max is None) or (left_max < node.data)) and ((right_min is None) or (right_min >node.data))
        mini = min(self.remove_nones([left_min,node.data,right_min]))
        maxi = max(self.remove_nones([left_max,node.data,right_min]))
        return(bst,mini,maxi)
    
    def isBST(self, root):
        #code here
        # main idea is that the max in the left side should be lesser than the node 
        # min in the right subtree should be greater than the node 
        
        isbst,mini,maxi = self.bst_check(root)
        return(isbst)




#{ 
 # Driver Code Starts
#Initial Template for Python 3
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
        s=input()
        root=buildTree(s)
        if Solution().isBST(root):
            print(1) 
        else:
            print(0)
# } Driver Code Ends