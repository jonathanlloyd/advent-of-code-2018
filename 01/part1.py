if __name__ == '__main__':
    frequency = 0
    with open('input', 'r') as input_file:
        for line in input_file:
            delta = int(line)
            frequency += delta
    print(f"Frequency: {frequency}")
