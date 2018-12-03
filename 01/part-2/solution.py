if __name__ == '__main__':
    answer = None
    seen_freqs = set()
    frequency = 0

    with open('input', 'r') as f:
        deltas = [int(line) for line in f.readlines()]

    while answer is None:
        for delta in deltas:
            seen_freqs.add(frequency)
            frequency += delta
            if frequency in seen_freqs:
                answer = frequency
                break

    print(f"First duplicate frequency: {answer}")
