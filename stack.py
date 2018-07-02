class Stack(object):
    def __init__(self, stack_list):
        self.stack_list = stack_list

    def is_empty(self):
        if not self.stack_list:
            return True

    def push(self, element):
        return self.stack_list.append(element)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]
