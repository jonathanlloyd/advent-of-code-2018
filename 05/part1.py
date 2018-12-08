from dataclasses import dataclass


def is_upper(string):
    return string == string.upper()

def is_lower(string):
    return string == string.lower()


@dataclass
class Element:
    value: str
    left: str = None
    right: str = None

    def __repr__(self):
        return f"Element(value='{self.value}', left={self.left is not None}, right={self.right is not None})"


if __name__ == '__main__':
    with open('input', 'r') as f:
        polymer = f.readline()

    polymer = polymer[:-1] # Remove trailing newline

    head = Element(value='')
    tail = Element(value='')
    prev = head
    for char in polymer:
        elem = Element(value=char)
        prev.right = elem
        elem.left = prev
        prev = elem
    elem.right = tail

    current_elem = head.right
    while current_elem is not tail:
        prev_elem = current_elem.left
        next_elem = current_elem.right
        should_react = (
            current_elem.value.lower() == next_elem.value.lower()
            and (
                (is_upper(current_elem.value) and is_lower(next_elem.value))
                or (is_lower(current_elem.value) and is_upper(next_elem.value))
            )
        )
        if should_react:
            next_next_elem = next_elem.right
            prev_elem.right = next_next_elem
            next_next_elem.left = prev_elem
            current_elem = prev_elem
        else:
            current_elem = next_elem

    result = ''
    current_elem = head.right
    while current_elem is not tail:
        result += current_elem.value
        current_elem = current_elem.right

    print(len(result))
