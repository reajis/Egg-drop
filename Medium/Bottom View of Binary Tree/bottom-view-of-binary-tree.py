#User function Template for python3

class Solution:
    def bottomView(self, root):
        self.maxLine =0
        self.minLine =0
        queue =[]
        queue.append(root)
        dicti ={}
        dicti[0] =root.data
        root.line =0
        currline =0
        while queue:
            curr_node= queue.pop(0)
            if curr_node.left:
                queue.append(curr_node.left)
                curr_node.left.line=curr_node.line -1
                dicti[curr_node.line -1] = curr_node.left.data
                self.minLine =min(self.minLine,curr_node.line -1)
                
            if curr_node.right:
                queue.append(curr_node.right)
                curr_node.right.line = curr_node.line +1
                dicti[curr_node.line +1] = curr_node.right.data
                self.maxLine =max(self.maxLine,curr_node.line +1)
        ans =[]
        for i in range(self.minLine,self.maxLine+1):
                    ans.append(dicti[i])
        return(ans)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
from collections import deque
from collections import defaultdict
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

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
        ob = Solution()
        res = ob.bottomView(root)
        for i in res:
            print (i, end = " ")
        print()


# } Driver Code Ends