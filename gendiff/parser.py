from pathlib import Path
import json
import yaml


class ErrorFormat(Exception):
    pass


def parse(data, data_format: str):
    if data_format == 'json':
        return json.loads(data)
    if data_format == 'yaml' or data_format == 'yml':
        return yaml.safe_load(data)
    raise ErrorFormat(f"This format is not supported: {data_format}")


def get_data(path):
    with open(path, "r") as data:
        return parse(data.read(), Path(path).suffix[1:])
