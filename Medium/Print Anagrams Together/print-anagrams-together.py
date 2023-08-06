#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        list_dicti = []
        list_answer = []
        for word in words:
            dicti = {}
            for letter in word:
                dicti[letter] = dicti.get(letter,0)+1
            list_dicti.append([dicti])
        #print(list_dicti)   
        while words:
            word = words.pop(0)
            list_curr =[]
            list_curr.append(word)
            ref = list_dicti.pop(0)
            #print("ref",ref)
            i=0
            while i<len(words) :
                #print("index",i)
                if ref == list_dicti[i]:
                    #print('yes',ref,list_dicti[i],i)
                    list_dicti.pop(i)
                    add = words.pop(i)
                    list_curr.append(add)
                    i-=1
                i+=1
            list_answer.append(list_curr)
                
                    
            
            
        #print("list_ans =", list_answer)   
        return(list_answer)
            
            
                
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends