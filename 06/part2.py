from dataclasses import dataclass

MAX_DIST = 10000


@dataclass
class Coord:
    x: int
    y: int


def parse_line(line):
    x_string, y_string = line.split(', ')
    return Coord(int(x_string), int(y_string))

def manhattan_dist(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.readlines()
    coords = [parse_line(line) for line in lines]

    smallest_x = min(c.x for c in coords)
    largest_x = max(c.x for c in coords)
    smallest_y = min(c.y for c in coords)
    largest_y = max(c.y for c in coords)

    matching_cell_count = 0
    for x in range(smallest_x, largest_x + 1):
        for y in range(smallest_y, largest_y + 1):
            cell = Coord(x, y)
            distances = [manhattan_dist(cell, coord) for coord in coords]
            total_distance = sum(distances)
            if total_distance < MAX_DIST:
                matching_cell_count += 1

    print(matching_cell_count)
