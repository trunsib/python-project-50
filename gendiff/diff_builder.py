def diff(d1, d2):
    res = []
    keys = sorted(d1.keys() | d2.keys())
    for key in keys:
        node = {'name': key}
        if key not in d1:
            node['status'] = 'added'
            node['data'] = d2[key]
        elif key not in d2:
            node['status'] = 'deleted'
            node['data'] = d1[key]
        elif type(d1[key]) is dict and type(d2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = diff(d1[key], d2[key])
        elif d1[key] == d2[key]:
            node['status'] = 'not changed'
            node['data'] = d1[key]
        else:
            node['status'] = 'changed'
            node['data before'] = d1[key]
            node['data after'] = d2[key]
        res.append(node)
    return res
