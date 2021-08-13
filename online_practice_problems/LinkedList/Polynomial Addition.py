# Given two polynomial numbers represented by a linked list. The task is to complete the function addPolynomial() that adds these lists meaning adds the coefficients who have the same variable powers.
# Note:  Given polynomials are sorted in decreasing order of power.

'''
 class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
'''

class Solution:
    # return a linked list denoting the sum with decreasing value of power
    def addPolynomial(self, poly1, poly2):
        p1=poly1
        p2=poly2
        result=node(0,0)
        r=result
        while p1 is not None and p2 is not None:
            if p1.power==p2.power:
                r.next=node(p1.coef+p2.coef,p1.power)
                r=r.next
                p1=p1.next
                p2=p2.next
            elif p1.power>p2.power:
                r.next=node(p1.coef,p1.power)
                r=r.next
                p1=p1.next
            else:
                r.next=node(p2.coef,p2.power)
                r=r.next
                p2=p2.next
                
        if p1 is not None:
            r.next=p1
        if p2 is not None:
            r.next=p2
        result=result.next
        return result


# TODO:
# Without extra Space :  
