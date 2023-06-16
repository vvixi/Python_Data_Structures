'''
Binary Tree by vvixi in Python 3.10
Root node: the top most node with no parents
Parent node: has at least 1 child node
Child node: has a parent node
Leaf node: has no children
A binary tree has nodes with at most 2 children
a bt has only one path between root and any node
an empty tree is considered a valid tree ie: 0 nodes

'''

class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val)
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
        
        print(f'Head popped: {prev.val} : \t {self.head}\n')
class Node:
    
    def __init__(self, val: int):
        self.val: int = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.val}'

class BinaryTree:

    def __init__(self, nodes: list):
        self.root = None
        self.nodes = nodes
        self.q = LinkedList()
        #self.view: list = None

    def __repr__(self):
        return f'\n\t\t\t\t({self.root.val})\n\t\t({self.root.left})\t\t\t\t({self.root.right})' 
        #--{self.root.left}--{self.root.right}')
    
    def initTree(self):
        #self.view = [[" " for i in range(20)]for i in range(6)]
        for startingNode in self.nodes:
            self.addNode(startingNode)
    
    def addNode(self, newVal: int):
        current = self.root
        if current is None:
            self.root = Node(newVal)
            #self.view[0][6] = newVal
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
        #print(current)
        result.append(current)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    
    return result

def depthFirstRec(root) -> []:
    
    # base case
    if root == [] or root == None:
        return []
    leftVals = depthFirstRec(root.left) #b,d,e
    rightVals = depthFirstRec(root.right) #c,f
    
    result = [root] + leftVals + rightVals
    return result

# breadth first traversal
def breadthFirst(root) -> []:
    # should return a,b,c,d,e,f 
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
