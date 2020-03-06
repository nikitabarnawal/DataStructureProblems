#create a node
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

    #insert a new node at the end of the linkedlist
    def Endnode(self, new_data):
        #import pdb
        #pdb.set_trace()
        temp = self.head
        while(temp):
            new_node = Node(new_data)
            if temp.next == None:
                temp.next = new_node
                new_node.next = None
                break
            temp = temp.next

    #get the length of the linkedlist
    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count+= 1
            temp = temp.next

        return count

    #get the last node of the linkedlist
    def getEndNode(self):
        temp = self.head
        while(temp):
            if temp.next == None:
                return temp
            temp = temp.next
    
    #get previous node of last node from the last
    def getPreviousNode(self,node):
        temp = self.head
        while(temp):
            if temp.next == node:
                return temp
            temp = temp.next


    #checks whether a linkedlist is palindrome or not
    def isPalindrome(self):
        start = self.head
        end = self.getEndNode()
        nodescnt = self.getCount()
        cnt = nodescnt//2
        while(cnt):  
            if start.data != end.data:
                return False

            start = start.next
            end = self.getPreviousNode(end)
            
            cnt -= 1
        return True

    def deleteDuplicates(self):
        temp = self.head
        while temp.next is not None:
            if temp.data == temp.next.data:
                next = temp.next.next
                temp.next = next
            else:
                temp = temp.next
        return self.head

    def deleteDuplicateNode(self):
        pre = self.head
        curr = self.head
        temp = None
        Inloop = False
        while(curr and curr.next):
            if curr.data != curr.next.data:
                pre.next = curr
                pre = curr
                curr = curr.next
                if temp is None:
                    temp = self.head = pre
            else:
                val = curr.data
                while curr is not None and curr.data == val:
                    curr = curr.next

            Inloop = True
            

        if temp is None and Inloop:
            self.head = None
            
        return self.head
    
    def removeNthFromEnd(self,n):
        temp = self.head
        cnt = self.getCount()
        delNode = self.head
        for i in range(cnt-n):
            delNode = delNode.next

        prev = self.head
        #import pdb
        #pdb.set_trace()
        while(temp):
            if temp.data == delNode.data:
                next = temp.next
                prev.next = next
            else:
                prev = temp
                temp = temp.next

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end= ' ')
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.push(6)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(9)
    llist.push(10)
    llist.Endnode(11)
    #print(llist.isPalindrome())
    #llist.deleteDuplicates()
    #llist.removeNthFromEnd(4)
    #llist.deleteDuplicateNode()
    #print(llist.printList())

    
