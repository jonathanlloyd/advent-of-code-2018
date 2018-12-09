from dataclasses import dataclass


@dataclass
class Coord:
    x: int
    y: int


def parse_line(line):
    x_string, y_string = line.split(', ')
    return Coord(int(x_string), int(y_string))

def min_no_equal(iterable, key=None):
    if len(iterable) == 1:
        return iterable[0]
    elif len(iterable) == 0:
        return None

    sorted_iterable = sorted(iterable, key=key)
    if key(sorted_iterable[0]) == key(sorted_iterable[1]):
        return None

    return sorted_iterable[0]

if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.readlines()
    coords = [parse_line(line) for line in lines]

    smallest_x = min(c.x for c in coords)
    largest_x = max(c.x for c in coords)
    smallest_y = min(c.y for c in coords)
    largest_y = max(c.y for c in coords)

    width = largest_x - smallest_x
    height = largest_y - smallest_y

    pos_to_coord = {
        f"{coord.x - smallest_x}_{coord.y - smallest_y}": coord
        for coord in coords
    }

    grid = {}
    for x in range(0, width + 1):
        for y in range(0, height + 1):
            pos = f"{x}_{y}"
            coord_distances = {}
            for i, coord in enumerate(coords):
                coord_relative_x = coord.x - smallest_x
                coord_relative_y = coord.y - smallest_y

                coord_dist_x = abs(coord_relative_x - x)
                coord_dist_y = abs(coord_relative_y - y)


                total_dist = coord_dist_x + coord_dist_y
                coord_distances[i] = total_dist

            grid[pos] = coord_distances

    grid_mins = {}
    for pos, coord_distances in grid.items():
        min_dist = min_no_equal(coord_distances.items(), key=lambda x: x[1])
        if min_dist:
            grid_mins[pos] = min_dist[0]
        else:
            grid_mins[pos] = None
    
    infinites = set()
    # Scan left / right for infinites
    for y in range(0, height + 1):
        for x in [0, width]:
            pos = f"{x}_{y}"
            infinites.add(grid_mins[pos])
    # Top / bottom
    for y in [0, height]:
        for x in range(0, width + 1):
            pos = f"{x}_{y}"
            infinites.add(grid_mins[pos])

    """
    for y in range(0, height + 1):
        row = ''
        for x in range(0, width + 1):
            pos = f"{x}_{y}"
            coord = pos_to_coord.get(pos)
            min_elem = grid_mins[pos]
            if coord is not None:
                if min_elem in infinites:
                    row += 'I'
                else:
                    row += 'E'
            elif min_elem is None:
                row += '.'
            else:
                row += str(min_elem)
            row += ' '
        print(row)
    """

    coord_area_counts = {}
    for coord_index in grid_mins.values():
        if coord_index is None:
            continue
        elif coord_index not in infinites:
            coord_area_counts[coord_index] = coord_area_counts.get(coord_index, 0) + 1

    print(max(coord_area_counts.items(), key=lambda c: c[1]))
