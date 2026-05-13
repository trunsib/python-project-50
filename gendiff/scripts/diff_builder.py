def diff(d1, d2):
    res = []
    keys = sorted(d1.keys() | d2.keys())
    for key in keys:
        node = {'name': key}
        if key not in d1:
            node['type'] = 'added'
            node['value'] = d2[key]
        elif key not in d2:
            node['type'] = 'deleted'
            node['value'] = d1[key]
        elif type(d1[key]) is dict and type(d2[key]) is dict:
            node['type'] = 'nested'
            node['children'] = diff(d1[key], d2[key])
        elif d1[key] == d2[key]:
            node['type'] = 'unchanged'
            node['value'] = d1[key]
        else:
            node['type'] = 'changed'
            node['old_value'] = d1[key]
            node['new_value'] = d2[key]
        res.append(node)
    return res
