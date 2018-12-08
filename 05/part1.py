class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None


def should_react(a, b):
    return a.lower() == b.lower() and a != b

def react(polymer):
    stack = Stack()
    for unit in polymer:
        head = stack.peek()
        if head and should_react(unit, head):
            stack.pop()
        else:
            stack.push(unit)

    return ''.join(stack.items)


if __name__ == '__main__':
    with open('input', 'r') as f:
        polymer = f.readline()

    polymer = polymer.strip() # Remove trailing newline
    reduced_polymer = react(polymer)
    print(len(reduced_polymer))
