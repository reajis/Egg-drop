#User function Template for python3

def count(n):
    points =[3,5,10]
    arr = [[0 for cols in range(n+1)] for rows in range (3)]
    for j in range (n+1):
        if  j % points [0] ==0:
            arr[0][j] = 1 
    for i in range (1,3):
        for j in range(n+1):
            if j < points[i]:
                arr[i][j] = arr[i-1][j]
            else:
                
                arr[i][j] = arr[i-1][j] +arr[i][j-points[i]]
    return(arr[2][n])
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))
        
# } Driver Code Ends