# #
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
#
#
# class LinkedList:
#
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head =new_node
#         self.tail = new_node
#         self.length = 1
#


# my_linked_list = LinkedList(4)
#
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value = None):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            return temp.value

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop (self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1 # if is one item , we have just this
        if self.length == 0:
            self.head = None
            self.tail = None

        return  temp
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self,index, value):
        temp = self.get(index)
        if temp :
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove (self, index):
        if index < 0  or  index >= self.length:
            return  None

        if index==0 :
            return self.pop_first()
        if index == self.length :
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return  temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def interactive_linked_list():
    linked_list = LinkedList()

    while True:
        print("\n--- Linked List Operations ---")
        print("1. Print List")
        print("2. Append")
        print("3. Prepend")
        print("4. Insert at index")
        print("5. Remove at index")
        print("6. Pop (remove last)")
        print("7. Pop first")
        print("8. Reverse List")
        print("9. Find Middle Node")
        print("10. Check for Loop")
        print("0. Exit")

        choice = input("Choose an operation: ")

        if choice == '1':
            linked_list.print_list()

        elif choice == '2':
            value = int(input("Enter value to append: "))
            linked_list.append(value)

        elif choice == '3':
            value = int(input("Enter value to prepend: "))
            linked_list.prepend(value)

        elif choice == '4':
            index = int(input("Enter index to insert at: "))
            value = int(input("Enter value to insert: "))
            result = linked_list.insert(index, value)
            if result is None:
                print("Invalid index.")

        elif choice == '5':
            index = int(input("Enter index to remove: "))
            result = linked_list.remove(index)
            if result is None:
                print("Invalid index.")
            else:
                print(f"Removed value: {result}")

        elif choice == '6':
            result = linked_list.pop()
            if result is None:
                print("List is empty.")
            else:
                print(f"Popped value: {result}")

        elif choice == '7':
            result = linked_list.pop_first()
            if result is None:
                print("List is empty.")
            else:
                print(f"First popped value: {result}")

        elif choice == '8':
            linked_list.reverse()
            print("List reversed.")

        elif choice == '9':
            middle_value = linked_list.find_middle_node()
            print(f"Middle node value: {middle_value}")

        elif choice == '10':
            has_loop = linked_list.has_loop()
            print("Loop detected!" if has_loop else "No loop detected.")

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


# اجرای برنامه
interactive_linked_list()

#
# my_linked_list = LinkedList(0)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append("asghar")
# my_linked_list.append(7)
# my_linked_list.pop()
# my_linked_list.pop_first()
# my_linked_list.prepend(43)
# my_linked_list.set_value(2,55)
# my_linked_list.print_list()
# my_linked_list.insert(2, "sepy")
# my_linked_list.reverse()
# my_linked_list.print_list()
#



"--------------------------------------------------"


