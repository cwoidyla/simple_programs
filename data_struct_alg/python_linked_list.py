

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_dups(self):
        """
        Challenge: Write code to remove duplicates from an unsorted linked list
        """
        if self.head == None:
            return None
        dups = []
        curr = self.head
        prev = self.head
        while curr != None:
            if curr.data in dups:
                prev.next = curr.next
            else:
                dups.append(curr.data)
                prev = curr
            curr = curr.next

    def print_list(self):
        vals = []
        if self.head == None:
            return vals
        curr = self.head
        while curr != None:
            vals.append(curr.data)
            curr = curr.next
        return vals

if __name__ == '__main__':
    # Build linked list
    a = Node('apple')
    b = Node('bat')
    c = Node('cat')
    d = Node('bat')
    a.next = b
    b.next = c
    c.next = d

    # Add linked list
    llist = LinkedList()
    llist.head = a
    print(llist.print_list())
    print(llist.print_list())
    # Remove duplicates
    llist.remove_dups()
    print(llist.print_list())
