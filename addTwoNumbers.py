#%%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2listnode(x: list):
    for i, x_t in enumerate(x):
        if i == 0:
            x_ = ListNode(x_t)
        else:
            temp = ListNode(x_t)
            temp.next = x_
            x_ = temp
    return x_

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        temp = None
        while True:
            if l1 == None and l2 == None:
                break
            if l1 != None :
                t1 = l1.val
                l1 = l1.next
            else:
                t1 = 0
            if l2 != None:
                t2 = l2.val
                l2 = l2.next
            else:
                t2 = 0
            val = t1 + t2 + carry
            if val > 9:
                val -= 10
                carry = 1
            else:
                carry = 0
            
            l3 = ListNode(val)
            l3.next = temp
            temp = l3


        if carry == 1:
            l3 = ListNode(1)
            l3.next = temp
        
        temp = None
        while l3 != None:
            l4 = ListNode(l3.val)
            l4.next = temp
            temp = l4
            l3 = l3.next

        return l4
            


#%%
if __name__ == "__main__":
    n1 = [2,4,3,6]
    n2 = [5,6,4]


    l1 = list2listnode(n1)
    l2 = list2listnode(n2)

    solver = Solution()
    answer = solver.addTwoNumbers(l1,l2)
    print(answer)
    


# #%%
# a = answer

# #%%
# a.val


# #%%
# a = a.next

#%%
