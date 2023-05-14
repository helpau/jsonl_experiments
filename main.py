from llama_index import download_loader, GPTVectorStoreIndex
import json


UnstructuredURLLoader = download_loader("UnstructuredURLLoader")

urls = [
     "https://wiki.astralinux.ru",
     
]

loader = UnstructuredURLLoader(urls=urls, continue_on_failure=False, headers={"User-Agent": "value"})
json_lines=""
docs=loader.load()
for i in range(len(docs)):
     string=docs[i].text
     dct=dict()
     dct[i]=string
     json_line=json.dumps(dct,ensure_ascii=False)[1:-1]
     print(json_line)
print(docs)


