import re
import json

with open(
    r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\luat-an-ninh-quoc-gia.txt",
    encoding="utf8",
) as f:
    lines = f.readlines()

pattern: dict = {
    "chương": r"\bchương\s+(\d+|[IVXLCDM]+)\b",
    "điều": r"điều\s+(\d+)",
    "điểm": r"^\d+\.",
}


def indexExtract(docs,start,end, pattern) -> dict:
    Index = dict()
    List = []
    for i in range(start,end):
        match = re.search(pattern, docs[i].lower(), re.IGNORECASE)
        if match:
            List.append(match.group())
            StartEnd = dict()
            StartEnd["start"] = i
            StartEnd["end"] = len(docs)
            if len(List) > 1:
                Index[List[-2]]["end"] = i - 1
            Index[match.group()] = StartEnd
    return Index


def chuongExtract(docs,start,end, pattern) -> dict:
    Chuong = dict()
    for i in range(start,end):
        match = re.search(pattern, docs[i].lower(), re.IGNORECASE)
        if match:
            ChuongData = dict()
            ChuongData["tên"] = docs[i + 2][:-1]
            Chuong[match.group()] = ChuongData
    return Chuong


def dieuExtract(docs,start,end, pattern) -> dict:
    Dieu = dict()
    for i in range(start,end):
        match = re.search(pattern, docs[i].lower(), re.IGNORECASE)
        if match:
            DieuData = dict()
            DieuData["tên"] = docs[i][match.end() + 2 : -1]
            Dieu[match.group()] = DieuData
    return Dieu


def diemExtract(docs,start,end, pattern) -> dict:
    Diem = dict()
    for i in range(start,end):
        match = re.search(pattern, docs[i].lower(), re.IGNORECASE)
        if match:
            DiemData = dict()
            DiemData["tên"] = docs[i][match.end() + 1 : -1]
            Diem[match.group()] = DiemData
    return Diem


def extract(docs, pattern):
    Luat = dict()
    Luat = chuongExtract(docs,start=0,end= len(docs),pattern= pattern["chương"])
    ChuongIndex = indexExtract(docs,start=0,end= len(docs),pattern= pattern["chương"])
    for x, y in ChuongIndex.items():
        Dieu = dieuExtract(docs, y['start'],y['end'],pattern=pattern['điều'])
        DieuIndex = indexExtract(docs, y['start'],y['end'],pattern=pattern['điều'])
        Luat[x]['điều'] = Dieu
        for z, w in DieuIndex.items():
            Diem =diemExtract(docs,w['start'],w['end'],pattern['điểm'])
            Luat[x]['điều'][z]['điểm'] =Diem
    return Luat

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

data = extract(lines,pattern)
file_name = "luat-an-ninh-quoc-gia.json"
with open(file_name, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)