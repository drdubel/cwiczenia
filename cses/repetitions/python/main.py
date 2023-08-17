import re

print(max(map(len, re.findall(r"A+|T+|G+|C+", input()))))
