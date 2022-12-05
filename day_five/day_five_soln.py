#!/usr/bin/python3

from collections import deque

def parse_input(input_file):
    with open(input_file, 'r') as f:
        stacks, instructions = f.read().split('\n\n')

    return stacks.splitlines(), instructions.splitlines()

def get_columns(stacks):
    columns = {stack_no: deque() for stack_no in range(1, len(stacks)+1)}

    for row in stacks[:-1]:
        for index, row_index in enumerate(range(1,len(row),4),1):
            if row[row_index].strip():
                columns[index].append(row[row_index])
                
    return columns

def get_final_str(columns, res_str):
    for x in columns.values():
        res_str += x[0]
        
    return res_str  

def part_one():
    stacks, instructions = parse_input('input.txt')
    columns = get_columns(stacks)

    for move in instructions:
        num_to_move, from_stack, to_stack = [int(x) for x in move.split() if x.isdigit()]
        moved_items = deque()

        for i in range(num_to_move):
            moved_items.appendleft(columns[from_stack].popleft())
        
        if len(moved_items) > 1:
            moved_items.reverse()

        columns[to_stack].extendleft(moved_items)
    
    return get_final_str(columns, '')
    
def part_two():
    stacks, instructions = parse_input('input.txt')
    columns = get_columns(stacks)

    for move in instructions:
        num_to_move, from_stack, to_stack = [int(x) for x in move.split() if x.isdigit()]
        moved_items = deque()

        for i in range(num_to_move):
            moved_items.appendleft(columns[from_stack].popleft())
        
        columns[to_stack].extendleft(moved_items)
    
    return get_final_str(columns, '')
    
result_p1 = part_one()    
result_p2 = part_two()  
