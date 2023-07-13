#User function Template for python3

class Solution:
   
    
    def findMin(self, arr, n):
        start = 0
        end = n-1
        while (start != end):
            mid = (start+end)//2
            
            if arr[mid]>arr[end]:
                start = mid +1
            else :
                if mid ==0:
                    if arr[0]>arr[1]:
                        start = mid +1
                    else:
                        end = mid -1
                if arr[mid]>arr[mid-1]:
                    end = mid -1
                else:
                    return(arr[mid])
         
        if start == end :
            return(arr[start])
        return(arr[start])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends