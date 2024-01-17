import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    keys = sorted(data1.keys() | data2.keys())
    added = data2.keys() - data1.keys()
    removed = data1.keys() - data2.keys()
    result = []
    for key in keys:
        if key in removed:
            result.append(f'  - {key}: {data1[key]}')
        elif key in added:
            result.append(f'  + {key}: {data2[key]}')
        elif data1[key] == data2[key]:
            result.append(f'    {key}: {data1[key]}')
        else:
            result.append(f'  - {key}: {data1[key]}\n  + {key}: {data2[key]}')
    result_in_string = ('\n'.join(result))
    return f"{{\n{result_in_string}\n}}"
