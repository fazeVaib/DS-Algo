class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = SinglyLinkedListNode(data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def printSinglyLinkedList(node):
    while(node):
        print(str(node.data))
        node = node.next


def insertNodeAtPosition(head, data, position):
    n = head
    for _ in range(position - 1):
        n = n.next
    nnext = n.next
    n.next = SinglyLinkedListNode(data)
    n.next.next = nnext

    return head

if __name__ == "__main__":
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())
    pos = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, pos)

    printSinglyLinkedList(llist_head)

    
