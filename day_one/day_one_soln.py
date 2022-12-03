#!/usr/bin/python3

def get_calorie_sums(input_file):
    with open(input_file, 'r') as file: 
        return [sum(map(int, line.split('\n'))) for line in file.read().strip().split('\n\n')]

def part_one():
    calorie_sums = sorted(get_calorie_sums('input.txt'), reverse=True)
    top_three = calorie_sums[:3]
    result = sum(top_three)

    return result

result_p1 = part_one()    
