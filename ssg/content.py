import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(cls.metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if self.data["type"] else None
    
    @property.setter
    def type(self, value):
        self.data["type"] = value

    def __getitem__(self, key):
        return self.data.get(key)

    def __iter__(self):
        for key, value in self.data.items():
            yield(key, value)
    
    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        return str(data)
        for key, value in self.data.items():
            if key != self.content:
                data[key] = value