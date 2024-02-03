def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()
    result = {}
    for key in keys:
        description = {"key": key}
        if key in deleted:
            description["operation"] = 'deleted'
            description["value"] = data1[key]
        elif key in added:
            description["operation"] = 'added'
            description["value"] = data2[key]
        elif data1[key] == data2[key]:
            description["operation"] = 'unchanged'
            description["value"] = data1[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            description["operation"] = 'nested'
            description["value"] = build_diff(data1[key], data2[key])
        else:
            description["operation"] = 'changed'
            description["old"] = data1[key]
            description["new"] = data2[key]
        result[key] = description
    return result
