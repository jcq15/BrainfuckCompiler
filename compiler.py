#-*- coding:utf-8 -*-

import msvcrt

point = 0               # 指针位置
pro_point = 0           # 程序源文件的指针
cache = [0 for i in range(0,100)]   # 初始化list

def right():
    global point
    if point + 1 >= len(cache):
        cache.append(0)
    point = point + 1

def left():
    global point
    if point == 0:
        print("Error! Want to left when point is at position 0!")
        exit()
    else:
        point = point - 1

def add():
    global cache
    cache[point] += 1

def minus():
    global cache
    cache[point] -= 1

def bout():
    print(chr(cache[point]))

def bin(c):
    global cache
    cache[point] = ord(c)

def start_block(pro_index, program):
    global pro_point
    num = 0                 # a stack
    if cache[point] == 0:
        for i in range(pro_index, len(program)):
            if program[i] == '[':
                num += 1    # push into stack
            elif program[i] == ']':
                num -= 1    # out of stack
                if num == 0:
                    pro_point = i
                    return
        print("Error! Can't match \'[\' and \']\'!")

def end_block(pro_index, program):
    global pro_point
    i = pro_index
    num = 0
    while i >= 0:
        if program[i] == ']':
            num += 1
        elif program[i] == '[':
            num -= 1
            if num == 0:
                pro_point = i-1
                return
        i -= 1
    print("Error! Can't match \'[\' and \']\'!")

if __name__ == '__main__':
    with open('program.txt', 'r') as file:
        program = file.read()
        lenth = len(program)

    while pro_point < lenth:
        word = program[pro_point]
        # print(word)
        if word == '>':
            right()
        elif word == '<':
            left()
        elif word == '+':
            add()
        elif word == '-':
            minus()
        elif word == '.':
            bout()
        elif word == ',':
            c = msvcrt.getch()
            bin(c)
        elif word == '[':
            start_block(pro_point, program)
        elif word == ']':
            end_block(pro_point, program)
        else:
            pass
        #print(cache[:10])
        #print(point)
        pro_point += 1
