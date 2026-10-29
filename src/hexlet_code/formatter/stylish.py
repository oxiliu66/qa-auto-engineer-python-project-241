def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)

def format_style(diff):
    lines = []
    for item in diff:
        status = item[0]
        key = item[1]

        if status == 'unchanged':
            value = format_value(item[2])
            lines.append(f'    {key}: {value}')
        elif status == 'removed':
            value = format_value(item[2])
            lines.append(f'  - {key}: {value}')
        elif status == 'added':
            value = format_value(item[2])
            lines.append(f'  + {key}: {value}')
        elif status == 'changed':
            old_val = format_value(item[2])
            new_val = format_value(item[3])
            lines.append(f'  - {key}: {old_val}')
            lines.append(f'  + {key}: {new_val}')
    if not lines:
        return '{}'
    return '{\n' + '\n'.join(lines) + '\n}'