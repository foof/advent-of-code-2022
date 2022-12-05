

draw_map = {'A': 'X', 'B': 'Y', 'C': 'Z'}
win_map = {'A': 'Y', 'B': 'Z', 'C': 'X'}
lose_map = {'A': 'Z', 'B': 'X', 'C': 'Y'}
map_map = {'X': lose_map, 'Y': draw_map, 'Z': win_map}
points = {'X': 1, 'Y': 2, 'Z': 3}


def get_score(a, b):
    score = points[b]
    if b == win_map[a]:
        score += 6
    elif b == draw_map[a]:
        score += 3

    return score


def part1(lines):
    score = 0
    for line in lines:
        a, b = line.split(' ')
        score += get_score(a, b)

    return score


def part2(lines):
    score = 0
    for line in lines:
        a, b = line.split(' ')
        score += get_score(a, map_map[b][a])

    return score


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(part1(list(lines)))
        print(part2(list(lines)))
