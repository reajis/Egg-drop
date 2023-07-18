#User function Template for python3

class Solution:
    def pos(mid):
        pass
    
    def search(self, A : list, l : int, r : int, key : int):
        
        while l !=r and l< r :
            
            mid = (l+r)//2
            #print(l,mid,r,A[l],A[mid],A[r])

            if A[mid] == key :
                return(mid)
  
            if A[mid] > A[r]:
                if key > A[r] and key < A[mid]:
                    #print('test1')
                    r = mid-1
                else:
                    #print('test3')
                    l = mid+1
                
            elif A[mid]<A[r]:
                if key <= A[r] and key > A[mid]:
                    
                    #print('test3')
                    l = mid+1
                else:
                    #print('test4')
                    r = mid-1
        #print(l,r,A[l])
        if A[l] ==key:
            
            return(l)
        else:
            return(-1)
        
        
        
                
                
        
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends