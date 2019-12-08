
#Remove every kth node linkedlist
#Given a singly linked list, your task is to remove every kth node from the linked list.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #insert a new node at the beginning of the linkedlist
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def deletek(self,k):
        i = 0
        temp = self.head
        n = k
        if k == 1:
            return None
        while(temp.next):
            i += 1
            if i == k-1:
                temp.next = temp.next.next
                k = k + (n-1)
                
            if temp.next:
                temp =temp.next

        return self.head

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end= ' ')
            temp = temp.next


if __name__=='__main__':
    llist = LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.deletek(3)
    print(llist.printList())
