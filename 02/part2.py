if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.readlines()

    lines.sort()

    line_1 = None
    line_2 = None
    varying_letter_index = None

    for i, line in enumerate(lines[:-1]):
        neighbour = lines[i+1]
        num_different_letters = 0
        for j, letter in enumerate(line):
            neighbours_letter = neighbour[j]
            if neighbours_letter != letter:
                varying_letter_index = j
                num_different_letters += 1
            if num_different_letters > 1:
                break

        if num_different_letters == 1:
            line_1 = line
            line_2 = neighbour
            break

    answer = line_1[:varying_letter_index] + line_1[varying_letter_index + 1:]

    print(f"Box code: {answer}")
