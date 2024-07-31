import re
import json


pattern: dict = {
    "chương": r"\bchương\s+(\d+|[IVXLCDM]+)\b",
    "điều": r"điều\s+(\d+)",
    "điểm": r"^\d+\.",
}


def indexExtract(docs, start, end, pattern) -> dict:
    Index = dict()
    List = []
    for i in range(start, end):
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


def chuongExtract(docs, start, end, pattern) -> dict:
    List = []
    for i in range(start, end):
        match = re.search(pattern, docs[i].lower(), re.IGNORECASE)
        if match:
            ChuongData = dict()
            ChuongData["id"] = match.group()[-1]
            ChuongData["ten"] = docs[i + 2][:-1]
            List.append(ChuongData)
    return List


def dieuExtract(docs, start, end, pattern) -> dict:
    List = []
    for i in range(start, end):
        match = re.search(pattern, docs[i].lower(), re.IGNORECASE)
        if match:
            DieuData = dict()
            DieuData["id"] = match.group()[-1]
            DieuData["ten"] = docs[i][match.end() + 2 : -1]
            List.append(DieuData)
    return List


def diemExtract(docs, start, end, pattern) -> dict:
    List = []
    for i in range(start, end):
        match = re.search(pattern, docs[i].lower(), re.IGNORECASE)
        if match:
            DiemData = dict()
            DiemData["id"] = match.group()[0]
            DiemData["ten"] = docs[i][match.end() + 1 : -1]
            List.append(DiemData)
    return List


def extract(docs, pattern):
    Luat = []
    Chuong = chuongExtract(docs, start=0, end=len(docs), pattern=pattern["chương"])
    ChuongIndex = indexExtract(docs, start=0, end=len(docs), pattern=pattern["chương"])
    chuongPosition = 0
    for x, y in ChuongIndex.items():
        Dieu = dieuExtract(docs, y["start"], y["end"], pattern=pattern["điều"])
        Luat.append({"chuong": Chuong[chuongPosition]})
        DieuIndex = indexExtract(docs, y["start"], y["end"], pattern=pattern["điều"])
        Luat[chuongPosition]["chuong"]["dieu"] = Dieu
        dieuPosition = 0
        for z, w in DieuIndex.items():
            Diem = diemExtract(docs, w["start"], w["end"], pattern["điểm"])
            Luat[chuongPosition]["chuong"]["dieu"][dieuPosition]["diem"] = Diem
            dieuPosition += 1
        chuongPosition += 1
    return Luat


def pretty(d, indent=0):
    for key, value in d.items():
        print("\t" * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print("\t" * (indent + 1) + str(value))


file_names = ["luat-bao-chi", "luat-an-ninh-quoc-gia", "luat-bao-hiem-xa-hoi"]

for file_name in file_names:
    txt_file_path = (
        r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\{}.txt".format(
            file_name
        )
    )
    json_file_path = (
        r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\{}.json".format(
            file_name
        )
    )

    with open(txt_file_path, encoding="utf8") as f:
        lines = f.readlines()

    data = extract(lines, pattern)
    finalData = {"ten": "BẢO HIỂM XÃ HỘI", "ngay": "19/03/203", "noi_dung": data}

    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(finalData, json_file, ensure_ascii=False, indent=4)
