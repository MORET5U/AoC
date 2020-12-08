import os
from typing import Counter

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as fp:
    raw_data = fp.read()

groups = raw_data.split("\n\n")
groups_straightened = [set(group.replace("\n", "")) for group in groups]

groups_calculated = [len(group) for group in groups_straightened]
result1 = sum(groups_calculated)

print(f"part 1 — {result1}")
