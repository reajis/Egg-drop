MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def multiplyTwoList(head1, head2):
    num1=0
    num2 =0
    curr1 =head1
    while curr1:
        num1 = num1*10 +curr1.data
        curr1 =curr1.next
    #print(num1)
    curr2 =head2
    while curr2:
        num2 = num2*10 +curr2.data
        curr2=curr2.next
    #print(num2)
    return(int(num1*num2)%MOD)




#{ 
 # Driver Code Starts
class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(ptr):
    while ptr!=None:
        print(ptr.data, end=" ")
        ptr= ptr.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        # printlist(list1.get_head())
        # print ''
        list2 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list2.insert(i)
        # printlist(list2.get_head())
        # print ''
        print(multiplyTwoList(list1.get_head(), list2.get_head()))

# } Driver Code Ends