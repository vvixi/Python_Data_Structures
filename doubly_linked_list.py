# Doubly Linked List in Python 3.10 by vvixi

class Node:

    def __init__(self, val: str):

        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        
        return f'<- {self.val} -> {self.next}'

class LinkedList:
    '''A doubly linked list is a linear data structure. The nodes in a dll contain pointers
    to both the previous and next nodes in the list. The two pointers in each node allow for
    traversal in both directions. Each node also contains a data field symbolized here with
    integers. Access and search operations are O(n), while insertion and deletion are O(1).'''    
    
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
        # set current's prev pointer to prev node
        current.prev = prev

        print(f'New tail added: {self.tail.val} \t {self.head}\n')
    
    def dequeue(self) -> Node:
        
        # remove the head, update the next node to the head
        prev = self.head
        self.head = prev.next
        
        print(f'Head dequeued: {prev.val} : \t {self.head}\n')
        return prev

    def push(self, val):
        # needs tested
        node = Node(val)
        prev = self.head
        current = node
        prev.prev = current
        current.next = prev
        self.head = node

    def pop(self) -> Node:
        # double check this matches stack code
        return self.tail

    def search(self, val) -> Node:
        
        # this method demonstrates traversal
        current = self.head
        while current != None:
            if current.val == val:
                # print and return the node if it is found
                print(f'Node: {current.val} was found\n')
                return current
        
            else:
                current = current.next
        
        return None
        print(f'Node: {val} was not found\n')

    def delete(self, val):
        
        # cases: node is tail, node is head, node is middle
        node = self.search(val)
        if node is not None:
            if node is self.head:
                self.dequeue()
            
            elif node is self.tail:
                # the previous node's next now points to None
                node.prev.next = None
            
            # if the node is neither head nor tail
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            print(f'Node {val} removed. \t {self.head}')
            return

dll = LinkedList()
dll.enqueue(1)
dll.enqueue(2)
dll.enqueue(3)
dll.enqueue(4)
dll.enqueue(5)
dll.dequeue()
dll.dequeue()
dll.delete(4)

