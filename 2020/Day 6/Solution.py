import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as fp:
    raw_data = fp.read()

groups = raw_data.split("\n\n")
groups = [set(group.replace("\n", "")) for group in groups]

groups_calculated = [len(group) for group in groups]
result1 = sum(groups_calculated)

print(f"Part 1 — {result1}")

groups = [[set(answers) for answers in group.split("\n")] for group in raw_data.split("\n\n")]

result2 = 0
for group in groups:
    result2 += len(group[0].intersection(*group[1:]))

print(f"Part 2 — {result2}")
