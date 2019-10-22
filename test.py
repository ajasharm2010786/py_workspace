
import csv
import pandas as pd
import json
import sys

# https://medium.com/@yzhong.cs/serialize-and-deserialize-complex-json-in-python-205ecc636caa

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(json.dumps(j))

with open('F:\\test2.json', 'r') as f:
    data = json.load(f)
    for d in data:
        p = Payload(d)
        for k, v in p.answers.items():
            if isinstance(v, dict):
                print(v)



    
