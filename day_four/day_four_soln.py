#!/usr/bin/python3

def parse_input(input_file):
    with open(input_file, "r") as f:
        sections = [section.strip().split(',') for section in f.readlines()]
    return sections


def both_soln():
    part_one_total = 0 
    part_two_total = 0 

    sections = parse_input('input.txt')
    for pair in sections:
        elf_one, elf_two = pair

        start_one, finish_one = elf_one.split('-')
        start_two, finish_two = elf_two.split('-')

        if (int(start_one) <= int(start_two) and int(finish_one) >= int(finish_two)):
            part_one_total += 1

        elif (int(start_two) <= int(start_one) and int(finish_two) >= int(finish_one)):
            part_one_total += 1

        if (int(start_one) <= int(finish_two) and int(finish_one) >= int(start_two)):
            part_two_total += 1

    return part_one_total, part_two_total

result_p1 = part_one()    
result_p2 = part_two()    
