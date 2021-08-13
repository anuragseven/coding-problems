# For each test case output will be an integer denoting the product of the two linked list.

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
    p1=head1
    p2=head2
    num1=''
    num2=''
    
    while p1 is not None:
        num1+=str(p1.data)
        p1=p1.next
    while p2 is not None:
        num2+=str(p2.data)
        p2=p2.next
    
    result=int(num1)*int(num2)
    return result%MOD