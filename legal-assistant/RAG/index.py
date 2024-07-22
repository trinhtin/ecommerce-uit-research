import re

string = "chương 1111: asdfkjsa;dlfkjasdf"

match = re.search("chương[^:]*:", string)

print(match)
