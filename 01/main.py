#!/usr/bin/env python

def run_a(file: str) -> int:
    prev_int = None
    ascend = 0
    with open(file) as input_file:
        file_content = input_file.read().split('\n')
    for line in file_content:
        if prev_int is None:
            prev_int = int(line)
        if prev_int < int(line):
            ascend += 1
        prev_int = int(line)
    return ascend


def run_b(file: str) -> int:
    prev_value = None
    ascend = 0
    with open(file) as input_file:
        file_content = input_file.read().split('\n')
    for index, line in enumerate(file_content):
        if len(file_content) <= index + 2:
            continue
        if prev_value is None:
            prev_value = int(file_content[index]) + int(file_content[index + 1]) + int(file_content[index + 2])
        elif prev_value < int(file_content[index]) + int(file_content[index + 1]) + int(file_content[index + 2]):
            ascend += 1
        prev_value = int(file_content[index]) + int(file_content[index + 1]) + int(file_content[index + 2])
    return ascend


if __name__ == "__main__":
    assert run_a('test.txt') == 7
    print('a: ' + str(run_a('input.txt')))
    assert run_b('test.txt') == 5
    print('b: ' + str(run_b('input.txt')))
