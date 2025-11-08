def create_plain(d_list):
    d_list.sort(key=lambda x: x['name'])
    res = get_diff_plain(d_list)
    return '\n'.join(res)


def get_diff_plain(d_list, path=''):
    res = []
    for node in d_list:
        path_to_ch = path + node['name']
        match node['status']:
            case 'nested':
                path_to_ch += '.'
                diff = get_diff_plain(node['children'], path_to_ch)
                res.extend(diff)
            case 'added':
                ch = сonvert_to_string(node['data'])
                diff = (f"Property '{path_to_ch}' was added "
                        f"with value: {ch}")
                res.append(diff)
            case 'deleted':
                ch = сonvert_to_string(node['data'])
                diff = "Property '{}' was removed".format(path_to_ch)
                res.append(diff)
            case 'changed':
                ch_bef = сonvert_to_string(node['data before'])
                ch_aft = сonvert_to_string(node['data after'])
                diff = (f"Property '{path_to_ch}' was updated. "
                        f"From {ch_bef} to {ch_aft}")
                res.append(diff)
            case 'not changed':
                continue
            case _:
                raise ValueError('Invalid type!')
    return res


def сonvert_to_string(data):
    if type(data) is dict or type(data) is list:
        res = '[complex value]'
    elif data is False or data is True:
        res = str(data).lower()
    elif data is None:
        res = 'null'
    elif type(data) is str:
        res = "'{}'".format(data)
    else:
        res = '{}'.format(data)
    return res
