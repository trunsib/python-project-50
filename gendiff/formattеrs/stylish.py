def create_stylish(d_list, depth=0):
    """Format diff list to stylish string format."""
    indent = '    ' * depth
    current_indent = '    ' * (depth + 1)
    
    lines = ['{']
    
    for node in sorted(d_list, key=lambda x: x['name']):
        name = node['name']
        status = node['status']
        
        if status == 'nested':
            value = create_stylish(node['children'], depth + 1)
            lines.append(f"{current_indent}{name}: {value}")
        
        elif status == 'added':
            value = convert_to_string(node['data'])
            lines.append(f"{current_indent}+ {name}: {value}")
        
        elif status == 'deleted':
            value = convert_to_string(node['data'])
            lines.append(f"{current_indent}- {name}: {value}")
        
        elif status == 'changed':
            old_value = convert_to_string(node['data before'])
            new_value = convert_to_string(node['data after'])
            lines.append(f"{current_indent}- {name}: {old_value}")
            lines.append(f"{current_indent}+ {name}: {new_value}")
        
        elif status == 'not changed':
            value = convert_to_string(node['data'])
            lines.append(f"{current_indent}  {name}: {value}")
    
    lines.append(f"{indent}}}")
    
    result = '\n'.join(lines)
    return result + '\n'


def convert_to_string(value):
    """Convert a value to string representation."""
    if isinstance(value, dict):
        if not value:
            return '{}'
        lines = ['{']
        for k, v in sorted(value.items()):
            lines.append(f"    {k}: {convert_to_string(v)}")
        lines.append('}')
        return '\n'.join(lines)
    
    if isinstance(value, bool):
        return str(value).lower()
    
    if value is None:
        return 'null'
    
    if isinstance(value, str):
        return value
    
    return str(value)
