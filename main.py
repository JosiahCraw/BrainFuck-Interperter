import sys
from collections import deque

codes = ['+', '-', '<', '>', '.', ',', '[', ']']

current_pointer = 0
memory = [0] * 10000000
std_out = deque()
std_in = deque()

def print_stream():
    global current_pointer, memory, std_out, std_in
    string = str(chr(memory[current_pointer]))
    std_out.append(string)
    if (string is '\n'):
        std_out.pop()
        print(*std_out, sep='')
        std_out = deque()
        return

def operate(program_code, max_size):
    global current_pointer, memory, std_out, std_in
    program_pointer = 0
    working_stack = []
    counter_stack = []

    while 1:
        if program_pointer >= max_size:
            break
        code = program_code[program_pointer]
        if code is '+':
            memory[current_pointer] += 1
            if memory[current_pointer] > 255:
                memory[current_pointer] = 0
            program_pointer += 1
            continue
        elif code is '-':
            memory[current_pointer] -= 1
            if memory[current_pointer] < 0:
                memory[current_pointer] = 255
            program_pointer += 1
            continue
        elif code is '<':
            current_pointer -= 1
            program_pointer += 1
            continue
        elif code is '>':
            current_pointer += 1
            program_pointer += 1
            continue
        elif code is '.':
            # print(chr(memory[current_pointer]))
            print_stream()
            program_pointer += 1
            continue
        elif code is ',':
            usr_in = input()
            memory[current_pointer] = ord(usr_in[0])
            program_pointer += 1
            continue
        elif code is '[':
            if memory[current_pointer] is 0:
                working_stack.append(code)
                while len(working_stack) is not 0:
                    program_pointer += 1
                    code = program_code[program_pointer]
                    working_stack.append(code)
                    if code is ']':
                        while 1:
                            temp = working_stack.pop()
                            if temp is '[':
                                break
                program_pointer += 1
                continue
            else:
                counter_stack.append(program_pointer)
                program_pointer += 1
                continue
        elif code is ']':
            program_pointer = counter_stack.pop()
            continue

                


if __name__ == "__main__":
    file_name = sys.argv[1]
    file = open(file_name, "r")
    data = file.readlines()
    program = []
    for line in data:
        for char in line:
            if char in codes:
                program.append(char)
    tempOut = open("stripped.bf", "w+")
    max_size = 0
    for char in program:
        tempOut.write(char)
        max_size += 1
    operate(program, max_size)

    file.close()