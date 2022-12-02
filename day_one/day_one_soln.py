#!/usr/bin/python3

def get_calorie_sums(input_file):
    with open(input_file, 'r') as file: 
        return [sum(map(int, line.split('\n'))) for line in file.read().strip().split('\n\n')]

calorie_sums = sorted(get_calorie_sums('input.txt'), reverse=True)
top_three = calorie_sums[:3]
answer = sum(top_three)


print(top_three)
