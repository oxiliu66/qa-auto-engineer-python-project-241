from .stylish import format_value

def build_diff(data1, data2):
    result = []
    all_keys = sorted(set(data1) | set(data2))
    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result.append(('unchanged', key, data1[key]))
            else:
                result.append(('changed', key, data1[key], data2[key]))
        elif key in data1:
            result.append(('removed', key, data1[key]))
        else:
            result.append(('added', key, data2[key]))

    return result