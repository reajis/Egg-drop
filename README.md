# Egg-drop
 
#### time complexity = O(k*N) and space complexity = O(k*N) 

### Problem Statement
Given a building with k floors and n eggs, find the minimum number of drops needed to find a floor from which it is safe to drop an egg without breaking it.
## Constraints:
1. An egg that survives a fall can be used again.
2. A broken egg must be discarded.
3. The effect of a fall is the same for all eggs.
4. If an egg breaks when dropped, then it would break if dropped from a higher floor.
5. If an egg survives a fall then it would survive a shorter fall.
## EXAMPLE CASE HAVING 10 FLOORS
If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop it from the second-floor window. Continue upward until it breaks. In the worst case, this method may require k-1 droppings.

now if two eggs are available we can reduce this even further by perhaps we can split the floor into sections and checking it out section by section
however, instead of taking a random section, we need to find the floor we should  start dropping the egg such that no of drops are minimum

##  dynamically arriving at the solution
#### we define our base conditions as : 
#### when we have n eggs and 1. 0 floors -> 0 drop 
#### when we have n eggs and 2. 1 floor -> 1 drop
bow we can calculate for the remaining cases 
there are two possibilities for egg to drop from a floor
It Breaks
It doesn’t Break

The first possibility suggests that all the floors above the floor k break the egg. So none of them is threshold but the ones below floor k including floor k are possible candidates. stating that now we have e-1 number of eggs and k-1 number of floors to check. Hence, to look at the eggDrop(e-1,k-1).

On the other hand, the second suggests that the floors below the floor k also do not break the egg and are not threshold floors and floors above the floor k are the possible candidates. stating that we still have e number of eggs and f-k (total floors -the floor k) the number of floors to check. Hence, to look at eggDrop(e,f-k).

Now, From these two possibilities we have to select the maximum one since we have to select the worst case

therefore, max( eggDrop(e-1,k-1) , eggDrop(e,f-k) )
so we find the worst case no of dropping when we chose a particular floor as the floor from which we would first drop the egg (we find this for every floor and choose the optimum floor ie the min of all these values )  

### bottom up method 
approach is to make a k*n array representing the eggs and floors and fill it one by one by using information from the previous cells
eggDrop(e,f) = 1+min{max( eggDrop(e-1,k-1) , eggDrop(e,f-k) ) , k in 1:f}

##### references 
[https://medium.com/@parv51199/egg-drop-problem-using-dynamic-programming-e22f67a1a7c3](https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/)
