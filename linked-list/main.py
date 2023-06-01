
class node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:

    # Function to initialize head

    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning

    def push_to_front(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a new node at the end

    def push_to_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        # Assign the variable 'last' to the head
        last = self.head
        # while last.next != None ... while 'last' doesn't point to null
        while last.next:
            # last equals next node, therefore, last is the last node that is mainly pointing to null
            last = last.next
        # let last point to the new node created, therefore, the last node is pointing to the new node, making the new node the last node of the list
        last.next = new_node

    # Function to reverse the linked list

    def reverse(self):
        prev = None
        current = self.head
        if current is None:
            return
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to print the linked list

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, " => ", end="")
            temp = temp.next

    # Function to get the length of the linked list

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    # Function to remove a specific node from the linked list

    def remove(self, key):

        temp = self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
    # Search for the key to be deleted, keep track of the
    # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if key was not present in linked list
        if(temp == None):
            return
        # Unlink the node removed from linked list
        # Link the previous node to the node after the node removed
        prev.next = temp.next
        temp = None

    def sort(self):
        current = self.head
        next = None
        if current is None:
            return
        while current is not None:
            next = current.next
            while next is not None:
                if current.data > next.data:
                    swap(next.data, current.data)
                    next.data, current.data = current.data, next.data
                next = next.next
            current = current.next


def swap(first, second):
    first, second = second, first


my_list = linked_list()

print("\n\nAdding 1 to 5")
my_list.push_to_end(1)
my_list.push_to_end(2)
my_list.push_to_end(3)
my_list.push_to_end(4)
my_list.push_to_end(5)

my_list.display()


print("\n\nAdding 0 to the front")
my_list.push_to_front(0)
my_list.display()

print("\n\nAdding -1 to the front")
my_list.push_to_front(-1)
my_list.display()

print("\n\nAdding 6 to the end")
my_list.push_to_end(6)
my_list.display()


print("\n\nRemoving -1")
my_list.remove(-1)
my_list.display()


print("\n\nRemoving 6")
my_list.remove(6)
my_list.display()


print("\n\nFinal Linked List")
my_list.display()


my_list.reverse()
print("\nReversed Linked List")
my_list.display()
print("\nSorted Linked List")
my_list.sort()
my_list.display()
print("\n\n")