# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.

def flatten(root):
    if root.next is None:
        return root
    h=root
    
    while h.next is not None:
        hv=h.next
        v=root
        while v.bottom is not None and hv is not None:
            if v.data>=hv.data:
                t=Node(hv.data)
                t.bottom=v
                root=t
                v=root
                hv=hv.bottom
            elif v.bottom.data<hv.data:
                v=v.bottom
            else:
                t=Node(hv.data)
                t.bottom=v.bottom
                v.bottom=t
                hv=hv.bottom
                v=v.bottom
        while v.bottom is not None:
            v=v.bottom
            
        v.bottom=hv
        
        h.next=h.next.next
            
        
            
        
    
    return root