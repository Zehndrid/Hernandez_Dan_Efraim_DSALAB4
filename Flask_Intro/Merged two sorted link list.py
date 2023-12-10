#Hernandez, Dan Efraim V. BsCPE 2-6
#Lab 6 exercises(individual) Merge Link Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count


def merge_sorted_lists(list1, list2):
    merged_stack = Stack()

    current1 = list1.top
    current2 = list2.top

    while current1 is not None or current2 is not None:
        if current1 is None:
            merged_stack.push(current2.data)
            current2 = current2.next
        elif current2 is None:
            merged_stack.push(current1.data)
            current1 = current1.next
        elif current1.data < current2.data:
            merged_stack.push(current1.data)
            current1 = current1.next
        else:
            merged_stack.push(current2.data)
            current2 = current2.next

    merged_list = Stack()
    while not merged_stack.is_empty():
        merged_list.push(merged_stack.pop())

    return merged_list



stack1 = Stack()
stack2 = Stack()

stack1.push(5)
stack1.push(4)
stack1.push(2)
stack1.push(1)

stack2.push(5)
stack2.push(5)
stack2.push(4)
stack2.push(3)
stack2.push(2)
stack2.push(1)


result = merge_sorted_lists(stack1, stack2)

print("Merged List:")
result.print_stack()
