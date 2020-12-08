import os.path

# My brain is extremely small, so I used this solution from Medium: https://cnille.medium.com/advent-of-code-2020-day-05-solutions-ac74dd602ee6

with open(os.path.join(__file__, "../input.txt"), mode="r", encoding="utf-8") as fp:
    data = [line.removesuffix("\n") for line in fp.readlines()]


def get_seat_id(seat):
    transformation = {"F": "0", "B": "1", "L": "0", "R": "1"}
    binary = "".join([transformation[x] for x in seat])
    return int(binary, 2)


ids = [get_seat_id(x) for x in data]

print(f"Part 1 — {max(ids)}")

for i in range(max(ids)):
    low = i - 1
    high = i + 1
    if low in ids and high in ids and i not in ids:
        print(f"Part 2 — {i}")
