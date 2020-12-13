import os
import re
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as fp:
    raw_data = fp.read()

TARGET = "shiny gold"


bags = defaultdict(dict)
for line in raw_data.splitlines():
    bag = re.match(r"(.*) bags contain", line).groups()[0]
    for count, b in re.findall(r"(\d+) (\w+ \w+) bag", line):
        bags[bag][b] = int(count)


answer1 = set()


def search1(color):
    for b in bags:
        if color in bags[b]:
            answer1.add(b)
            search1(b)


search1(TARGET)
print(f"Part 1 — {len(answer1)}")


def search2(bag):
    count = 1
    for s in bags[bag]:
        multiplier = bags[bag][s]
        count += multiplier * search2(s)
    return count


print("Part 2 — {}".format(search2("shiny gold") - 1))

# idk this is such a weird concept to my small freaking brain, so i used someone else's solution
# credits: https://dev.to/cnille/advent-of-code-2020-day-07-3da8
