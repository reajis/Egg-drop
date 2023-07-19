#User function Template for python3



def maxArea(A,l):
    start = 0
    end = l -1
    water =0
    while start < end :
        breadth = end - start
        height = min(A[start],A[end])
        water = max (water , breadth*height)
        if A[start]>A[end]:
            end -=1
        elif  A[start]==A[end] :
            if A[start+1]>A[end-1]:
                start+=1
            else :
                end -=1
        else:
            start +=1
    #print(start,end,height,breadth)
    return(water)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends