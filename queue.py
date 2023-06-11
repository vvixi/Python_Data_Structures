# Linked List Queue in Python 3.10 by vvixi

class Node:

    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

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

queue = LinkedList()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
queue.search('C')
queue.search('Z')
queue.dequeue()
queue.dequeue()
