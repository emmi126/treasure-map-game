import random
from treasure_utilities import *

def generate_treasure_map_row(w, is3D):
    char_collect = ""
    move_symbol = w * 5/6
    empty_symbol = 1 - move_symbol
    for i in range(5):
        index = random.randint(0,3)
        char_collect += MOVEMENT_SYMBOLS[index]
    for j in range(1):
        char_collect += EMPTY_SYMBOL

    str_row = ""
    for k in range(w):
        index = random.randint(0,5)
        str_row += char_collect[index]

    if is3D == True:
        replace = random.randint(0,w-1)
        index = random.randint(0,1)
        probability = random.randint(0,1)
        if probability == 1:
            str_row = str_row[:replace] + MOVEMENT_SYMBOLS_3D[index] + str_row[replace+1:]

    return str_row

def generate_treasure_map(w, h, is3D):
    treasure_map = ">"
    for i in range(h):
        treasure_map += generate_treasure_map_row(w, is3D)
    return treasure_map[:-1]

def generate_3D_treasure_map(w, h, d):
    treasure_map_3D = generate_treasure_map(w, h, True)
    for i in range(d-1):
        for i in range(h):
            treasure_map_3D += generate_treasure_map_row(w, True)
    return treasure_map_3D

def follow_trail(str, row_index, col_index, depth_index, w, h, d, num_tiles):
    if row_index >= h or col_index >= w or depth_index >= d:
        return str

    treasure_count = 0
    symbol_count = 0

    currentSymbol = str[depth_index * w * h + row_index * w + col_index]
    while currentSymbol != 'X' and num_tiles != 0:

        if str[depth_index * w * h + row_index * w + col_index] in MOVEMENT_SYMBOLS + MOVEMENT_SYMBOLS_3D:
            str = change_char_in_3D_map(
                str, col_index, row_index, depth_index, "X", w, h, d)

        if currentSymbol == '>':
            col_index += 1
        elif currentSymbol == '<':
            col_index -= 1
        elif currentSymbol == 'v':
            row_index += 1
        elif currentSymbol == '^':
            row_index -= 1
        elif currentSymbol == '|':
            depth_index += 1
        elif currentSymbol == '*':
            depth_index -= 1

        col_index %= w
        row_index %= h
        depth_index = depth_index % d

        newSymbol = str[depth_index * w * h + row_index * w + col_index]

        if newSymbol == '+':
            treasure_count += 1

        if newSymbol not in '.+':
            currentSymbol = newSymbol

        num_tiles -= 1
        symbol_count += 1

    print('Treasures collected: {}'.format(treasure_count))
    print('Symbols visited: {}'.format(symbol_count))
    return str
