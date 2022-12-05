
import string


def find_priority(a: str, b: str) -> int:
    for C in a:
        if C in b:
            if C.lower() == C:
                return string.ascii_lowercase.index(C)+1
            else:
                return string.ascii_uppercase.index(C)+1+26


def find_priority_2(a: str, b: str, c: str) -> int:
    for C in a:
        if C in b and C in c:
            if C.lower() == C:
                return string.ascii_lowercase.index(C)+1
            else:
                return string.ascii_uppercase.index(C)+1+26


def part1(lines):
    result = 0
    for line in lines:
        result += find_priority(line[:len(line)//2], line[len(line)//2:])
    return result


def part2(lines):
    groups = []
    for i, line in enumerate(lines):
        if i % 3 == 0:
            groups.append([])
        groups[-1].append(line)

    result = 0
    for group in groups:
        result += find_priority_2(group[0], group[1], group[2])
    return result


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(part1(list(lines)))
        print(part2(list(lines)))
