
def part1(elves):
    elves = [sum([int(x) for x in elf.splitlines()]) for elf in elves]
    return max(elves)


def part2(elves):
    elves = sorted([sum([int(x) for x in elf.splitlines()]) for elf in elves])
    return sum(elves[-3:])


if __name__ == "__main__":
    with open('./input', 'r') as f:
        elves = f.read().split('\n\n')
        print(part1(elves))
        print(part2(elves))
