import random


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# constructs a random binary tree , n is number of nodes
def constructBinaryTree(n):
    if n <= 0:
        return
    if n == 1:
        return Node(random.randint(n, n ** 2))
    root = Node(random.randint(n, n ** 2))
    nodesList = [root]
    for i in range(n - 1):

        newNode = Node(random.randint(i, n ** 2))

        while True:
            randomIndex = random.randint(0, len(nodesList) - 1)
            randomNode = nodesList[randomIndex]
            if randomNode.right is None and randomNode.left is None:
                directionFlag = random.randint(0, 1)
                if directionFlag:
                    randomNode.right = newNode

                else:
                    randomNode.left = newNode
                break
            elif randomNode.right is None and randomNode.left is not None:
                randomNode.right = newNode
                break
            elif randomNode.right is not None and randomNode.left is None:
                randomNode.left = newNode
                break
        nodesList.append(newNode)

    return root


def inorderTraversal(root):
    if root is None:
        return []

    inorderTraversal(root.left)
    print(root.val)
    inorderTraversal(root.right)


def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)


def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)


def countCompletes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    if root.left is not None and root.right is not None:
        return 1 + countCompletes(root.left) + countCompletes(root.right)
    if root.left is not None or root.right is not None:
        return countCompletes(root.left) + countCompletes(root.right)


def isCompleteBinaryTree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        return False
    return True and isCompleteBinaryTree(root.left) and isCompleteBinaryTree(root.right)


def heightOfTheBinaryTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return 1 + max(heightOfTheBinaryTree(root.left), heightOfTheBinaryTree(root.right))


def addNodeInBST(root, val):
    if root is None:
        return
    prev = None
    curr = root
    while curr is not None:
        prev = curr
        if curr.val >= val:
            curr = curr.left
        else:
            curr = curr.right

    if prev.left is None and prev.right is None:
        if prev.val >= val:
            prev.left = Node(val)
        else:

            prev.right = Node(val)
        return
    if prev.left is None:
        prev.left = Node(val)
    else:

        prev.right = Node(val)


def constructBST(l):
    if len(l) == 0:
        return
    if len(l) == 1:
        return Node(l[0])
    root = Node(l[0])
    for i in range(1, len(l)):
        addNodeInBST(root, l[i])
    return root


def maxBST(root):
    if root is None:
        return

    temp = root
    while temp.right is not None:
        temp = temp.right

    return temp.val


def minBST(root):
    if root is None:
        return
    temp = root
    while temp.left is not None:
        temp = temp.left
    return temp.val


def deleteNodeFromBST(root, val):
    if root is None:
        return

    parent = None
    current = root

    while current is not None and current.val != val:
        parent = current
        if current.val > val:
            current = current.left
        else:
            current = current.right
    if current is None or parent is None:
        return
    # Leave case
    if current.left is None and current.right is None:
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
        return
    # if the node contains two child
    if current.left is not None and current.right is not None:

        leastNodeInRST = current.right
        if leastNodeInRST.left is None and leastNodeInRST.right is None:

            leastNodeInRST.left = current.left
            current.right = None
            if parent.left is current:
                parent.left = leastNodeInRST
            else:
                parent.right = leastNodeInRST
            return
        pOfLeastNodeInRST = None
        while leastNodeInRST.left is not None:
            pOfLeastNodeInRST = leastNodeInRST
            leastNodeInRST = leastNodeInRST.left

        pOfLeastNodeInRST.left = None
        leastNodeInRST.left = current.left
        leastNodeInRST.right = current.right
        if parent.left is current:
            parent.left = leastNodeInRST
        else:
            parent.right = leastNodeInRST
        return

    # if the node has one left child
    if current.left is not None:
        if parent.left is current:
            parent.left = current.left
        else:
            parent.right = current.left
        return
    # if the node has one right child
    if current.right is not None:
        if parent.left is current:
            parent.left = current.right
        else:
            parent.right = current.right
        return


def constructBTFromInorderPreorder(ino, preo):
    if ino is None or len(ino) == 0:
        return
    root = Node(preo[0])
    rootIndex = ino.index(root.val)
    leftST = ino[:rootIndex]
    rightST = ino[rootIndex + 1:]
    preLST = preo[1:len(leftST) + 1]
    preRST = preo[len(leftST) + 1:]
    root.left = constructBTFromInorderPreorder(leftST, preLST)
    root.right = constructBTFromInorderPreorder(rightST, preRST)
    return root


def constructBTFromInorderPostOrder(ino, posto):
    if ino is None or len(ino) == 0:
        return

    root = Node(posto[len(posto) - 1])
    rootIndex = ino.index(root.val)
    inLST = ino[:rootIndex]
    inRST = ino[rootIndex + 1:]
    postLST = posto[:len(posto) - 1 - len(inRST)]
    postRST = posto[len(postLST):len(posto) - 1]
    root.left = constructBTFromInorderPostOrder(inLST, postLST)
    root.right = constructBTFromInorderPostOrder(inRST, postRST)
    return root


root = constructBTFromInorderPostOrder([1, 2, 3, 4, 5, 6, 7, 8], [2, 1, 4, 3, 7, 8, 6, 5])
inorderTraversal(root)
