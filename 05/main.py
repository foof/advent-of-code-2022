import re


def part1(stacks, instructions):
    for inst in instructions:
        result = re.search(r"move ([0-9]*) from ([0-9]*) to ([0-9]*)", inst)
        amount, f, t = int(result.group(1)), int(result.group(2)), int(result.group(3))
        for i in range(int(amount)):
            stacks[t].append(stacks[f].pop())
    result = ''
    for key, value in stacks.items():
        result += value[-1]
    return result


def part2(stacks, instructions):
    for inst in instructions:
        result = re.search(r"move ([0-9]*) from ([0-9]*) to ([0-9]*)", inst)
        amount, f, t = int(result.group(1)), int(result.group(2)), int(result.group(3))
        move = stacks[f][-amount:]
        stacks[f] = stacks[f][0:-amount]
        stacks[t] = stacks[t] + move
    result = ''
    for key, value in stacks.items():
        result += value[-1]
    return result


if __name__ == "__main__":
    with open('./input', 'r') as f:
        stacks_input, instructions = f.read().split('\n\n')
        stacks_input = list(reversed(stacks_input.splitlines()))
        stacks = {}
        for i, num in enumerate(stacks_input[0]):
            if num == ' ':
                continue
            stacks[int(num)] = []
            for line in stacks_input[1:]:
                if line[i] != ' ':
                    stacks[int(num)].append(line[i])
        # print(part1(stacks, list(instructions.splitlines())))
        print(part2(stacks, list(instructions.splitlines())))
