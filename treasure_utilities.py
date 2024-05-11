MOVEMENT_SYMBOLS = '><v^'
MOVEMENT_SYMBOLS_3D = '*|'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'

def get_nth_row_from_map(str, n, w, h):
    if n >= h:
        return ""
    nth_row = str[w*n: w*(n+1)]
    return nth_row

def print_treasure_map(str, w, h):
    for i in range(h):
        print(get_nth_row_from_map(str, i, w, h))

def change_char_in_map(str, col_index, row_index, c, w, h):
    if row_index >= h or col_index >= w:
        return str
    index = (row_index) * w + col_index
    str_new = str[:index] + c + str[index+1:]
    return str_new

def get_proportion_travelled(str):
    if len(str) == 0:
        return
    breadcrumbs = 0
    for i in range(len(str)):
        if str[i] == BREADCRUMB_SYMBOL:
            breadcrumbs += 1
    proportion = breadcrumbs / len(str)
    return round(proportion, 2)

def get_nth_map_from_3D_map(str, n, w, h, d):
    if n > d:
        return ""
    nth_map = str[w*h*n : w*h*(n+1)]
    return nth_map

def print_3D_treasure_map(str, w, h, d):
    for i in range(d):
        map2d = get_nth_map_from_3D_map(str, i, w, h, d)
        print_treasure_map(map2d, w, h)
        if (i != d-1):
            print('')

def change_char_in_3D_map(str, col_index, row_index, depth_index, c, w, h, d):
    if row_index >= h or col_index >= w or depth_index >= d:
        return str
    index = w * h * depth_index + (row_index) * w + col_index
    str_new = str[:index] + c + str[index + 1:]
    return str_new
