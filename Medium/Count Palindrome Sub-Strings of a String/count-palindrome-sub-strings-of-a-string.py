#User function Template for python3

class Solution:

    def CountPS(self, s,n):
        n = len(s)
        tot =0
        for i in range(n):
            lp=i
            rp=i
            temp_ans=1
            while lp-1 >=0 and rp+1< n:
                lp-=1
                rp+=1
                if s[lp]==s[rp]:
                    temp_ans+=2
                else:
                    break
                if temp_ans >=2:
                    tot+=1
            
            if i+1< n and s[i]==s[i+1] :
                #print("yes")
                lp=i
                rp=i+1
                temp_ans=2
                tot+=1
                while lp-1 >=0 and rp+1< n:
                    lp-=1
                    rp+=1
                    if s[lp]==s[rp]:
                        temp_ans+=2
                    else:
                        break
                    if temp_ans >=2:
                        tot+=1
        return(tot)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.CountPS(S,N))
# } Driver Code Ends