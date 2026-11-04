def format_plain_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def format_plain(diff):
    lines = []
    for item in diff:
        status = item[0]
        key = item[1]

        if status == 'unchanged':
            continue
        elif status == 'removed':
            value = format_plain_value(item[2])
            lines.append(f"Property '{key}' was removed")
        elif status == 'added':
            value = format_plain_value(item[2])
            lines.append(f"Property '{key}' was added with value: {value}")
        elif status == 'changed':
            old_val = format_plain_value(item[2])
            new_val = format_plain_value(item[3])
            lines.append(f"Property '{key}' was updated. "
                         f"From {old_val} to {new_val}")
    return '\n'.join(lines)