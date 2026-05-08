def create_plain(diff_list, parent=''):
    """Format diff list to plain string format."""
    lines = []
    
    for node in diff_list:
        name = node['name']
        current_path = f"{parent}.{name}" if parent else name
        status = node['status']
        
        if status == 'nested':
            result = create_plain(node['children'], current_path)
            if result:
                lines.append(result)
        
        elif status == 'added':
            value = stringify_plain(node['data'])
            msg = "Property '" + current_path
            msg += "' was added with value: " + value
            lines.append(msg)
        
        elif status == 'deleted':
            lines.append("Property '" + current_path + "' was removed")
        
        elif status == 'changed':
            old_value = stringify_plain(node['data before'])
            new_value = stringify_plain(node['data after'])
            msg = "Property '" + current_path
            msg += "' was updated. From " + old_value
            msg += " to " + new_value
            lines.append(msg)
    
    return '\n'.join(lines)


def stringify_plain(value):
    """Convert a value to string representation for plain format."""
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return "'" + value + "'"
    return str(value)
