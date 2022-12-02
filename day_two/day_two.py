#!/usr/bin/python3

def parse_input(input_file):
    with open(input_file, "r") as f:
        for line in f.readlines():
            col_A, col_B = line.split()
            col_A, col_B = ord(col_A) - ord('A'), ord(col_B) - ord('X')
            yield (col_A, col_B)

def part_one():
    score = 0
    parsed_input = parse_input('input.txt')
    for opponent, player in parsed_input:
        score += player + 1
        score += ((player - opponent + 1) % 3) * 3
    return score

def part_two():
    score = 0 
    parsed_input = parse_input('input.txt')
    for opponent, outcome in parsed_input:
        score += outcome * 3
        score += ((opponent + outcome + 2) % 3) + 1
    return score

result_p1 = part_one()    
result_p2 = part_two()
