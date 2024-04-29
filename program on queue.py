class Queue:
    def __init__(self, size):
        self.stack = stack(size)

    def enqueue(self, val):
        self.stack.push_method(val)

    def dequeue(self):
        temp_stack = stack(len(self.stack.stack_list))
        while self.stack.stack_list:
            temp_stack.push_method(self.stack.stack_list.pop())
        if temp_stack.stack_list:
            temp_stack.stack_list.pop()
        while temp_stack.stack_list:
            self.stack.push_method(temp_stack.stack_list.pop())

    def display(self):
        temp_stack = stack(len(self.stack.stack_list))
        while self.stack.stack_list:
            temp_stack.push_method(self.stack.stack_list.pop())
        while temp_stack.stack_list:
            print(temp_stack.stack_list[-1])
            self.stack.push_method(temp_stack.stack_list.pop())

queue_1 = Queue(5)
while True:
    print("Select an option: 1. Enqueue 2. Dequeue 3. Display 4. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        num = int(input("Enter the number to enqueue: "))
        queue_1.enqueue(num)
    elif choice == 2:
        queue_1.dequeue()
    elif choice == 3:
        queue_1.display()
    elif choice == 4:
        break
    else:
        print("Invalid input")