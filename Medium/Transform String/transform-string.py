#Back-end complete function Template for Python 3

class Solution:
    def transform(self, A, B): 
        n1 = len(A)
        n2 = len(B)
        if n1 != n2:
            return(-1)
        dicti1 ={}
        dicti2 ={}
        
        for i in range (n1-1,-1,-1):
            dicti1[A[i]] = dicti1.get(A[i],0)+1
            dicti2[B[i]] = dicti2.get(B[i],0)+1
            
        if dicti1 != dicti2:
            #print(dicti1,dicti2)
            return(-1)
        p1=n1-1
        p2 =n2-1
        ans =0
        while p1 >=0:
            if A[p1]==B[p2]:
                p1 -=1
                p2 -=1
            else:
                ans +=1
                p1 -=1
        return(ans)
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A,B))
# } Driver Code Ends