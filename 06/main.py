
def find_position(line, num_unique):
    for i in range(num_unique, len(line)):
        # print("pos", i)
        S = set()
        for j in range(1, num_unique+1):
            # print(i-j)
            S.add(line[i-j])
        # print('---------')
        if len(S) == num_unique:
            return i


def part1(line):
    return find_position(line, 4)


def part2(line):
    return find_position(line, 14)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(part1(lines[0]))
        print(part2(lines[0]))
