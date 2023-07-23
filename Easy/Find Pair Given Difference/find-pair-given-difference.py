#User function Template for python3

class Solution:
    def binarySearch(self,arr, x):
        l =0
        r = len(arr)-1
 
        while l <= r:
     
            mid = l + (r - l) // 2
   
            if arr[mid] == x:
                return mid

            elif arr[mid] < x:
                l = mid + 1

            else:
                r = mid - 1

        return -1

    def findPair(self, arr, n,num):
        arr.sort()
        for i in range(n):
        
            comp = num + arr[i]
            pos = self.binarySearch(arr, comp)
            #print(comp,arr[i],pos)
            if pos != -1 and pos != i:
                return(True)
            

        return(False)
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends