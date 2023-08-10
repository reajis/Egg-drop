#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def append(root,value):
    curr = root
    while curr:
        if curr.data > value:
            if curr.left == None:
                curr.left = Node(value)
                break
            else:
                curr = curr.left
        else:
            if curr.right == None:
                curr.right = Node(value)
                break
            else:
                curr = curr.right
    return(root)
def post_order(pre, size) -> Node:
    root = Node(pre[0])
    if size <= 1:
        return(root)
    root.left= Node(pre[1])
    #if size >=2:
    for i in range(2,size):
        #print(pre[i])
        root = append(root,pre[i])
    return(root)
            
            
    
    
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data,end=' ')

if __name__ == '__main__':
    t=int(input())

    for _tcs in range(t):
        size=int(input())
        pre=[int(x)for x in input().split()]

        root=post_order(pre,size)

        postOrd(root)
        print()
# } Driver Code Ends