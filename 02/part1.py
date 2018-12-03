if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.readlines()

    num_lines_doubles = 0
    num_lines_triples = 0

    for line in lines:
        letter_counts = {}
        for letter in line:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

        for letter, count in letter_counts.items():
            if count == 2:
                num_lines_doubles += 1
                break

        for letter, count in letter_counts.items():
            if count == 3:
                num_lines_triples += 1
                break

    checksum = num_lines_doubles * num_lines_triples

    print(f"Checksum: {checksum}")
