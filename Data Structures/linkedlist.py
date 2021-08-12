# create a node :
class Node:
    value = None
    next = None


class LinkedList:
    def __init__(self, ):
        self.__header = None

    def addNode(self, value):
        if self.__header is None:
            self.__header = Node()
            self.__header.value = value
            return

        temp = self.__header
        while temp.next is not None:
            temp = temp.next
        newNode = Node()
        newNode.value = value
        temp.next = newNode

    def toList(self):
        listOfNodes = []
        pointer = self.__header
        while pointer is not None:
            listOfNodes.append(pointer.value)
            pointer = pointer.next
        return listOfNodes

    def pop(self):
        pointer = self.__header
        if pointer is None:
            return None
        if pointer.next is None:
            returnValue = self.__header.value
            self.__header = None
            return returnValue
        while pointer.next.next is not None:
            pointer = pointer.next
        returnValue = pointer.value
        pointer.next = None
        return returnValue

    def insert(self, index, value):
        iterate = index - 1
        pointer = self.__header

        if pointer is None:
            self.addNode(value)
            return

        if index == 0:
            newNode = Node()
            newNode.value = value
            newNode.next = self.__header
            self.__header = newNode
            return

        while iterate > 0 and pointer.next is not None:
            pointer = pointer.next
            iterate -= 1

        newNode = Node()
        newNode.value = value
        newNode.next = pointer.next
        pointer.next = newNode

    def remove(self, index):
        if self.__header is None:
            return

        if index == 0:
            self.__header = self.__header.next
            return

        iterate = index - 1
        pointer = self.__header
        while iterate > 0 and pointer.next is not None:
            pointer = pointer.next
            iterate -= 1
        if iterate == 0:
            pointer.next = pointer.next.next

    def getHeaderNode(self):
        return self.__header

    def setHeaderNode(self, header):
        self.__header = header


# print elements of a linked list in reverse order

def getElementsInReverse(l):
    if l is None:
        return []
    return getElementsInReverse(l.next) + [l.value]


# reverse a linked list


def reverseLinkedListInPlace(prev, curr, next, linkedList):
    if curr is None:
        linkedList.setHeaderNode(prev)
        return

    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    reverseLinkedListInPlace(prev, curr, next, linkedList)


def reverseLinkedListIterative(prev, curr, next, linkedList):
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    linkedList.setHeaderNode(prev)


linkedList = LinkedList()

for i in range(10):
    linkedList.addNode(i)
print(linkedList.toList())
reverseLinkedListIterative(None, linkedList.getHeaderNode(), None, linkedList)
print(linkedList.toList())
