def reverse(linked_list):
    if linked_list.length <= 1 :
        return linked_list
    else : 
        first = linked_list.head 
        second = first.next
        linked_list.tail = linked_list.head
        while second : 
            temp = second.next
            second = first.next
            linked_list.tail = linked_list.head 
            while second : 
                temp = second.next 
                second.next = first
                first = second 
                second = temp
            linked_list.head.next = None 
            linked_list.head = first 
            return linked_list
    
