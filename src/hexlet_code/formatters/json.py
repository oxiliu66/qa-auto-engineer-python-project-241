import json


def format_json(diff):
    lines = []
    for item in diff:
        status = item[0]
        key = item[1]
        if status == 'changed':
            old_val = item[2]
            new_val = item[3]
            lines.append({
                'status': status,
                'key': key,
                'old_value': old_val,
                'new_value': new_val
            })
        else:

            lines.append({
                'status': status,
                'key': key,
                'value': item[2]
            })
    return json.dumps(lines, indent=2)