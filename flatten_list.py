# Get a flat list without None, 0, empty lists, empty dicts, empty sets, empty tuples, empty ranges and empty string
# For example: input: [2, [3, 5, [1], [[32]], 3], None] output: [2, 3, 5, 1, 32, 3]

def execute(input_list):
    
    flat_list = []
    for i in input_list:
        if i== None:
            continue
        elif i == 0:
            continue
        elif i == '':
            continue
        elif i =={}:
            continue
        elif type(i) == list:
            print('recursion')
            flat_list += execute(i)
        else:
            flat_list.append(i)
    return flat_list