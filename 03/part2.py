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

    possible_answers = set([claim.ID for claim in claims])

    used_squares = {}
    for claim in claims:
        for i in range(0, claim.size.width):
            for j in range(0, claim.size.height):
                x = i + claim.position.x
                y = j + claim.position.y
                coords = f"{x}_{y}"
                if coords in used_squares:
                    prev_occupant_id = used_squares[coords]
                    possible_answers.discard(claim.ID)
                    possible_answers.discard(prev_occupant_id)
                used_squares[coords] = claim.ID

    assert len(possible_answers) == 1

    print(f"Isolated claim: {possible_answers.pop()}")
