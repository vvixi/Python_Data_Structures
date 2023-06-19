# Binary Search Tree in Python 3.10 by vvixi

class llNode:
    # node for Linked List class use
    def __init__(self, val: str):

        self.val = val
        self.next = None

    def __repr__(self):
        
        return f'{self.val} -> {self.next}'

class LinkedList:
    '''A queue is a FIFO linear data structure composed of nodes. They can be implemented
    with a linked list. Access and search operations are O(n), while insertion and deletion
    are O(1).'''    
    
    def __init__(self):
        
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, val):
        
        node = llNode(val)
        self.length += 1

        # set head and tail if there isn't one
        if self.head == None:
            self.head = self.tail = node
            print(f'\nNew head added: {self.head.val} \t {self.head}\n')
            return
        
        # set prev tail's next pointer to the new node         
        prev = self.tail
        current = node
        prev.next = current
        self.tail = current

        print(f'New tail added: {self.tail.val} \t {self.head}\n')
    
    def dequeue(self):
        
        # remove the head, update the next node to the head
        prev = self.head
        self.head = prev.next
        self.length -= 1

        print(f'Head popped: {prev.val} : \t {self.head}\n')
        return prev

    def search(self, val):
        
        # this method demonstrates traversal
        current = self.head
        while current != None:
            if current.val == val:
                # print and return the node if it is found
                print(f'Node: {current.val} was found\n')
                return current.val
            else:
                current = current.next

        print(f'Node: {val} was not found\n')

class Node:
    # node for the BST
    def __init__(self, val: int):
        
        self.val: int = val
        self.left = None
        self.right = None

    def __repr__(self):
        
        return f'{self.val}'

class BinaryTree:
    '''
    Root node: the top most node with no parents
    Parent node: has at least 1 child node
    Child node: has a parent node
    Leaf node: has no children
    A Binary Tree has nodes with at most 2 children
    and has only one path between root and any node
    an empty tree is considered a valid tree ie: 0 nodes
    '''
    def __init__(self, nodes: list):
        
        self.root = None
        self.nodes = nodes
        self.q = LinkedList()

    def initTree(self):
        
        for startingNode in self.nodes:
            self.addNode(startingNode)
    
    def addNode(self, newVal: int):
        
        current = self.root
        if current is None:
            self.root = Node(newVal)
            print(f'root node: {newVal} added successfully')
            return

        else:

            current = self.root
            while current is not None:
                if newVal < current.val:
                    if current.left is None:
                        current.left = Node(newVal)
                        print(f'left node {newVal} added successfully')
                        return
                    
                    elif current.left:
                        current = current.left

                elif newVal >= current.val:
                    if current.right is None:
                        current.right = Node(newVal)
                        print(f'right node {newVal} added successfully')
                        return
        
                    elif current.right:
                        current = current.right
        
bt = BinaryTree([5, 7, 1, 15, 9, 2, 8, 7, 3])
bt.initTree()

# iterative version
def depthFirstIter(root) -> []:
    
    if root == [] or root == None:
        return
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop(-1)
        result.append(current)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    
    return result

def depthFirstRec(root) -> []:
    
    if root == [] or root == None:
        return []
    leftVals = depthFirstRec(root.left)
    rightVals = depthFirstRec(root.right)
    
    result = [root] + leftVals + rightVals
    return result

def breadthFirst(root) -> []:
    
    if root == [] or root == None:
        return []

    values = []
    queue = [root]
    while len(queue) > 0:
        current = queue[0]
        values.append(current)
        queue = queue[1:]
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return values

print(f'Depth first iterative: {depthFirstIter(bt.root)}')
print(f'Depth first recursive: {depthFirstRec(bt.root)}')
print(f'Breadth first: {breadthFirst(bt.root)}')
