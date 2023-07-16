#User function Template for python3

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    
    def balance_chk(self,root,level,prev_level) :
        
        if root.left == None and root.right == None :
            
            if prev_level ==-10:
                #print("0",root.data)
                prev_level = level
                return(True,prev_level)
            elif level != prev_level:
                #print("1",root.data)
                return(False,prev_level)
            else:
                return(True,prev_level)
        else:
            if root.left: 
                #print("3",root.left.data)
                left_balance,prev_level= self.balance_chk(root.left,level+1,prev_level)

            if root.right:
                #print("4",root.right.data)
                right_balance ,prev_level= self.balance_chk(root.right,level+1,prev_level)

        if root.left == None: 
            #print("5",root.data)
            return(right_balance,prev_level)
            
        elif root.right == None:
            #print("7",root.data)
            return(left_balance,prev_level)
        else : 
            #print("8",root.data)
            is_balanced =(left_balance and right_balance) 
            return(is_balanced,prev_level)
        
    def check(self, root):
        balanced,prev_level = self.balance_chk(root,0,-10)
        #print(root)
        return(balanced)
        
        
        
        
        
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
        if Solution().check(root):
            print(1)
        else:
            print(0)



# } Driver Code Ends