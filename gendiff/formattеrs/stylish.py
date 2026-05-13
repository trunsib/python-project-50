def create_stylish(d_list, lvl=0):
    res = []
    res.append('{\n')
    ind = ' ' * 2
    ind = ind + ind * 2 * lvl
    d_list.sort(key=lambda x: x['name'])
    for node in d_list:
        op = ' '
        match node['type']:
            case 'nested':
                data = create_stylish(node['children'], lvl + 1)
            case 'added':
                data = сonvert_to_string(node['value'], ind)
                op = '+'
            case 'deleted':
                data = сonvert_to_string(node['value'], ind)
                op = '-'
            case 'changed':
                data = сonvert_to_string(node['old_value'], ind)
                res.append(f"{ind}- {node['name']}: {data}\n")
                data = сonvert_to_string(node['new_value'], ind)
                op = '+'
            case 'unchanged':
                data = сonvert_to_string(node['value'], ind)
            case _:
                raise ValueError('Invalid type!')
        res.append(f"{ind}{op} {node['name']}: {data}\n")
    res.append(ind[:-2] + '}')
    return ''.join(res)


def сonvert_to_string(data, ind):
    if type(data) is dict:
        ind = ind + '    '
        res = '{\n'
        for key in data.keys():
            value = сonvert_to_string(data[key], ind)
            res = res + ind + '  ' + key + ': ' + value + '\n'
        res = res + ind[:-2] + '}'
    elif data is False or data is True:
        res = str(value).lower()
    elif data is None:
        res = 'null'
    else:
        res = str(data)
    return res
