import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as fp:
    raw_data = fp.read()

instructions = raw_data.splitlines()


def execute(line: str, acc: int, index: int):
    instruction, arg = tuple(line.split())

    if instruction == "nop":
        index += 1
    elif instruction == "acc":
        acc += int(arg)
        index += 1
    elif instruction == "jmp":
        index += int(arg)

    return acc, index


def solve1():
    acc = 0
    index = 0
    seen: set[int] = set()

    while index != len(instructions):
        if index in seen:
            break

        seen.add(index)
        acc, index = execute(instructions[index], acc, index)
    return acc


print(f"Part 1 — {solve1()}")