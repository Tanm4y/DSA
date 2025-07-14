'''nodes have a memory address '''
'''end of list is null , in python it is none
class node has : node.value and node.next 
insertion and deletion is easier in O(1)
in case of a DLL there is also a node.prev'''

class SinglyNode: 
    def __init__(self , val , next = None):
        self.val = val
        self.next = next 

    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A =  SinglyNode(3)
B  = SinglyNode(4)
C = SinglyNode(7)

Head.next=A
A.next=B
B.next=C

print(Head)


#Traverse the list which is an O(n) operation 
curr = Head 
while curr :
    print(curr)
    curr = curr.next


#Display linked list - O(n)

def display(head):
    curr = head 
    elements =[]
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('->'.join(elements))

display(Head)


#Search for a node value O(n)

def search(head,val):
    curr = head 
    while curr :
        if val == curr.val:
            return True 
        curr = curr.next 
    return False 

print(search(Head,7))


#Doubly Linked List 

class DoublyNode: 
    def __init__(self , val , next = None , prev = None):
        self.val = val
        self.next = next
        self.prev = prev 

    def __str__(self):
        return str(self.val)


head = tail = DoublyNode(1)
print(tail)


#Display : 0(N)

def display(head):
    curr = head 
    elements =[]
    while curr : 
        elements.append(str(curr.val))
        curr = curr.next 
    print(' <-> '.join (elements))

display(head)

#Insert at begining ; O(1)

def insert_at_begining(head , tail , val):
    new_node = DoublyNode(val, next = head)
    head.prev = new_node
    return new_node , tail

head,tail = insert_at_begining(head, tail , 3 )
display(head)

# Insert at end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)