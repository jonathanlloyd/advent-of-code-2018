from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

@dataclass
class Size:
    width: int
    height: int

@dataclass
class Claim:
    ID: int
    position: Position
    size: Size

def parse_claim(string):
    parts = string.rstrip().split(' ')
    id_part = parts[0]
    ID = int(id_part[1:])

    position_part = parts[2][:-1]
    [x, y] = position_part.split(',')
    position = Position(int(x), int(y))

    size_part = parts[3]
    [width, height] = size_part.split('x')
    size = Size(int(width), int(height))

    return Claim(ID, position, size)


if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.readlines()
    
    claims = [parse_claim(line) for line in lines]

    used_squares = {}
    for claim in claims:
        for i in range(0, claim.size.width):
            for j in range(0, claim.size.height):
                x = i + claim.position.x
                y = j + claim.position.y
                coords = f"{x}_{y}"
                used_squares[coords] = used_squares.get(coords, 0) + 1

    num_overlapping_squares = 0
    for count in used_squares.values():
        if count > 1:
            num_overlapping_squares += 1

    print(num_overlapping_squares)
