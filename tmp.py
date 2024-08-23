import re

alma = "(6x1)(1x3)A"
match = re.search(r'\((\d+)x(\d+)\)', alma)
if match:
    print(alma)