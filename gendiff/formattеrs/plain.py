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
            lines.append(
                f"Property '{current_path}'was added with value: {
                    value}")
        
        elif status == 'deleted':
            lines.append(f"Property '{current_path}' was removed")
        
        elif status == 'changed':
            old_value = stringify_plain(node['data before'])
            new_value = stringify_plain(node['data after'])
            lines.append(
                f"Property '{current_path}' was updated. From {old_value} to {new_value}")
    
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
        return f"'{value}'"
    return str(value)
