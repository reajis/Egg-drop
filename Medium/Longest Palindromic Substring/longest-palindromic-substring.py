#User function Template for python3

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        best =0
        best_list=[]
        for i in range(n):
            lp=i
            rp=i
            temp_ans=1
            lis =[s[i]]
            while lp-1 >=0 and rp+1< n:
                lp-=1
                rp+=1
                if s[lp]==s[rp]:
                    temp_ans+=2
                    lis.insert(0,s[lp])
                    lis.append(s[rp])
                else:
                    break
            if temp_ans>best:
                best =temp_ans
                best_list =lis
            if i+1< n and s[i]==s[i+1] :
                #print("yes")
                lp=i
                rp=i+1
                temp_ans=2
                lis =[s[i],s[i+1]]
                while lp-1 >=0 and rp+1< n:
                    lp-=1
                    rp+=1
                    if s[lp]==s[rp]:
                        temp_ans+=2
                        lis.insert(0,s[lp])
                        lis.append(s[rp])
                    else:
                        break
                if temp_ans>best:
                    best =temp_ans
                    best_list =lis
            
        string =""
        for ele in best_list:
            string+= ele
        return(string)
             
                    
                
                
            
        
        
                    
                    
        
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends