

def part1(lines):
    result = 0
    for line in lines:
        a, b = line.split(',')
        a = [int(x) for x in a.split('-')]
        b = [int(x) for x in b.split('-')]
        if (a[0] <= b[0] and a[1] >= b[1]):
            result += 1
        elif (b[0] <= a[0] and b[1] >= a[1]):
            result += 1

    return result


def part2(lines):
    result = 0
    for line in lines:
        a, b = line.split(',')
        a = [int(x) for x in a.split('-')]
        b = [int(x) for x in b.split('-')]
        a = [x for x in range(a[0], a[1]+1)]
        b = [x for x in range(b[0], b[1]+1)]
        if len(set(a).intersection(b)):
            result += 1

    return result


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(part1(list(lines)))
        print(part2(list(lines)))
