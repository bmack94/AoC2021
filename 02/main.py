#!/usr/bin/env python

def run_a(file: str) -> int:
    depth = 0
    h_pos = 0
    with open(file) as input_file:
        file_content = input_file.read().split('\n')
    for line in file_content:
        instruction, amount = line.split(' ')
        if instruction == 'forward':
            h_pos += int(amount)
        elif instruction == 'up':
            depth -= int(amount)
        elif instruction == 'down':
            depth += int(amount)
    return depth * h_pos


def run_b(file: str) -> int:
    depth = 0
    h_pos = 0
    aim = 0
    with open(file) as input_file:
        file_content = input_file.read().split('\n')
    for line in file_content:
        instruction, amount = line.split(' ')
        if instruction == 'forward':
            h_pos += int(amount)
            depth += int(amount) * aim
        elif instruction == 'up':
            aim -= int(amount)
        elif instruction == 'down':
            aim += int(amount)
    return depth * h_pos


if __name__ == "__main__":
    assert run_a('test.txt') == 150
    print('a: ' + str(run_a('input.txt')))
    assert run_b('test.txt') == 900
    print('b: ' + str(run_b('input.txt')))
