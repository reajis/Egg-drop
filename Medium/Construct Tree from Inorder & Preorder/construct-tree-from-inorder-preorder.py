#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def rec_tree(self, inorder, preorder,start,end):
        if start>end:
            return
        root = Node(preorder[self.rootIndex])
        self.rootIndex +=1
        if start== end:
            return(root)
        for i in range(start,end+1):
            if inorder[i] ==root.data:
                break
        root.left= self.rec_tree( inorder, preorder,start,i-1)  
        root.right= self.rec_tree( inorder, preorder,i+1,end)  
        return(root)
        
    def buildtree(self, inorder, preorder, n):
        self.rootIndex =0
        root =self.rec_tree( inorder, preorder,0,n-1)
        return(root)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends