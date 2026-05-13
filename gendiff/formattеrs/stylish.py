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
                value = create_stylish(node['children'], lvl + 1)
            case 'added':
                value = сonvert_to_string(node['value'], ind)
                op = '+'
            case 'deleted':
                value = сonvert_to_string(node['value'], ind)
                op = '-'
            case 'changed':
                value = сonvert_to_string(node['old_value'], ind)
                res.append(f"{ind}- {node['name']}: {value}\n")
                value = сonvert_to_string(node['new_value'], ind)
                op = '+'
            case 'unchanged':
                value = сonvert_to_string(node['value'], ind)
            case _:
                raise ValueError('Invalid type!')
        res.append(f"{ind}{op} {node['name']}: {value}\n")
    res.append(ind[:-2] + '}')
    return ''.join(res)


def сonvert_to_string(value, ind):
    if type(value) is dict:
        ind = ind + '    '
        res = '{\n'
        for key in value.keys():
            value = сonvert_to_string(value[key], ind)
            res = res + ind + '  ' + key + ': ' + value + '\n'
        res = res + ind[:-2] + '}'
    elif value is False or value is True:
        res = str(value).lower()
    elif value is None:
        res = 'null'
    else:
        res = str(value)
    return res
