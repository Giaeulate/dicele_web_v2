""" Helpers """
# pylint: disable=too-few-public-methods, missing-class-docstring, missing-function-docstring
import json
from django.core import serializers


def convert_to_json(queryset=None, exclude=None):
    if queryset is None:
        queryset = {}

    if exclude is None:
        exclude = ['created', 'updated', 'active']

    response = []
    data = json.loads(serializers.serialize('json', queryset))
    for item in data:
        obj = item["fields"]
        obj["pk"] = item["pk"]
        for i in exclude:
            obj.pop(f'{i}', None)
        response.append(obj)
    return response
