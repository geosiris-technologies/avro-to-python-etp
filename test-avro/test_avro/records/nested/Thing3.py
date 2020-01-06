# -*- coding: utf-8 -*-

""" avro python class for file: Thing3 """

import json
from test_avro.helpers import default_json_serialize, todict
from typing import Union


class Thing3(object):

    schema = """
    {
        "type": "record",
        "name": "Thing3",
        "namespace": "records.nested",
        "fields": [
            {
                "name": "chars",
                "type": "string",
                "default": "string default"
            }
        ]
    }
    """

    def __init__(self, obj: Union[str, dict, 'Thing3']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'Thing3')"
            )

        self.set_chars(obj.get('chars', 'string default'))

    def dict(self):
        return todict(self)

    def set_chars(self, value: str) -> None:

        if isinstance(value, str):
            self.chars = value
        else:
            raise TypeError("field 'chars' should be type str")

    def get_chars(self) -> str:

        return self.chars

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)