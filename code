#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,eggs,floors):
       
        sol =[[0 for i in range(floors +1)]for j in range(eggs)] 
        for x in range(floors +1):
            sol[0][x]=x-1

        sol[0][0]=0

        for egg in range(1,eggs):
            for floor in range(floors+1):
                if floor == 0 or floor == 1:
                    sol[egg][floor]=0
                elif egg > floor:

                    sol[egg][floor] = sol[egg-1][floor]
                else :
                    mini = float('inf')
                    for tried_floor in range(1,floor+1):
                        maxi =1+max(sol[egg][floor-tried_floor],sol[egg-1][tried_floor-1])
                        mini = min(mini,maxi)
                    sol[egg][floor]= mini
        #print(sol)            
        return(sol[eggs-1][floors]+1)
        
