import re

with open(
    r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\luat-an-ninh-quoc-gia.txt",
    encoding="utf8",
) as f:
    lines = f.readlines()

pattern: dict = {"chương": r"\bchương\s+(\d+|[IVXLCDM]+)\b", "điều":r"điều\s+(\d+)"}


def indexExtract(docs, pattern):
    ChuongIndex=dict()
    ChuongList =[]
    for i in range(len(docs)):
        match = re.search(pattern['chương'], docs[i].lower(), re.IGNORECASE)
        if match:
            ChuongList.append(match.group())
            StartEnd = dict()
            StartEnd['start']=i
            if len(ChuongList)>1:
                ChuongIndex[ChuongList[-2]]['end'] = i-1
            ChuongIndex[match.group()] = StartEnd
    return ChuongIndex


def chuongExtract(docs,pattern):
    ChuongIndex = indexExtract(docs,pattern)
    Chuong = dict()
    i = 0
    for x,y in ChuongIndex.items():
        Chuong[x] = docs[int(y['start'])+2][:-1]
        try:
            dieuExtract(docs[y['start']:y['end']])
        except:
            dieuExtract(docs[y['start']:])
    return Chuong


def dieuExtract(docs):
    Dieu = dict()
    for i in range(len(docs)):
        if "điều" in docs[i].lower() and docs[i].lower().startswith("điều"):
            match = re.search(r"điều\s+(\d+)", docs[i].lower(), re.IGNORECASE)
            if match:
                print(match.group())
    
