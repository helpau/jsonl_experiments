import os
import io

import jsonlines


with jsonlines.open("ru_turbo_saiga.jsonl","r") as fin:
    print(fin.read())
