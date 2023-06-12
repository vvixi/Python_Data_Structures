class Node:

    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.prev} <- {self.val}'

class LinkedList:
    '''A stack is a LIFO linear data structure composed of nodes. They can be implemented
    with a linked list. Access and search operations are O(n), while insertion and deletion
    are O(1).'''
    
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def push(self, _val):
        node = Node(_val)
        self.length += 1
        if self.head == None:

            # set head and tail if this is the first node in stack
            self.head = self.tail = node
            print(f'\nNew head added: {self.head.val} \t {self.head}\n')
            return
        
        # set previous pointer on new node, set new node to head
        node.prev = self.head
        self.head = node
        print(f'New head added: {_val} \t {self.head}\n')
        
    def pop(self):
        self.length -= 1
        prevHead = self.head
        self.head = self.head.prev
        print(f'Popped head: {prevHead.val} : \t {self.head}\n')

    def peek(self):
        if self.head:
            print(f'Head: {self.head.val}\n')
            #return self.head
    
    def search(self, val):
        # method demonstrates traversal
        current = self.head
        while current != None:
            if current.val == val:
                # print and return the node if it is found
                print(f'Node: {current.val} was found\n')
                return current.val
            else:
                current = current.prev
        print(f'Node: {val} was not found\n')

stack = LinkedList()
stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')
stack.peek()
stack.search('A')
stack.search('X')
stack.pop()
stack.peek()
