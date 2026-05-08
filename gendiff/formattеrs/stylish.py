def create_stylish(diff_list, depth=0):
    """Format diff list to stylish string format."""
    indent = '    ' * depth
    current_indent = indent + '    '
    
    lines = ['{']
    
    for node in diff_list:
        name = node['name']
        status = node['status']
        
        if status == 'nested':
            value = create_stylish(node['children'], depth + 1)
            lines.append(f"{current_indent}{name}: {value}")
        
        elif status == 'added':
            value = stringify_value(node['data'])
            lines.append(f"{current_indent}+ {name}: {value}")
        
        elif status == 'deleted':
            value = stringify_value(node['data'])
            lines.append(f"{current_indent}- {name}: {value}")
        
        elif status == 'changed':
            old_value = stringify_value(node['data before'])
            new_value = stringify_value(node['data after'])
            lines.append(f"{current_indent}- {name}: {old_value}")
            lines.append(f"{current_indent}+ {name}: {new_value}")
        
        elif status == 'not changed':
            value = stringify_value(node['data'])
            lines.append(f"{current_indent}  {name}: {value}")
    
    lines.append(f"{indent}}}")
    return '\n'.join(lines)


def stringify_value(value):
    """Convert a value to string representation."""
    if isinstance(value, dict):
        if not value:
            return '{}'
        lines = ['{']
        for k, v in sorted(value.items()):
            lines.append(f"    {k}: {stringify_value(v)}")
        lines.append('}')
        return '\n'.join(lines)
    
    if isinstance(value, bool):
        return str(value).lower()
    
    if value is None:
        return 'null'
    
    if isinstance(value, str):
        return value
    
    return str(value)
