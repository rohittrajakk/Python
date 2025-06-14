class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")
            if n <= 0:
                raise Exception("Invalid index. Must be 1 or greater.")
            if n == 1:
                self.head = self.head.next
                return
            current = self.head
            for _ in range(n - 2):
                if not current.next:
                    raise Exception("Index out of range.")
                current = current.next
            if not current.next:
                raise Exception("Index out of range.")
            current.next = current.next.next
        except Exception as e:
            print("Error:", e)

ll = LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

print("Initial List:")
ll.print_list()

print("\nDeleting 3rd node:")
ll.delete_nth_node(3)
ll.print_list()

print("\nDeleting 10th node:")
ll.delete_nth_node(10)
