#!/usr/bin/python3

def parse_input(input_file):
    with open(input_file, "r") as f:
        sacks = f.read().split("\n")
    return sacks

def calc_priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27
   
def part_one():
    sacks = parse_input("input.txt")
    total = 0
    for sack in sacks:
        split_index=len(sack)//2
        part_1, part_2 = set(sack[:split_index]), set(sack[split_index:])
        common = (part_1 & part_2).pop()
        total += calc_priority(common)

    return total

def part_two():
    sacks = parse_input("input.txt")
    total = 0
    for index in range(0, len(sacks), 3):
        part_1, part_2, part_3 = set(sacks[index]), set(sacks[index+1]), set(sacks[index+2])
        common = (part_1 & part_2 & part_3).pop()
        total += calc_priority(common)

    return total
