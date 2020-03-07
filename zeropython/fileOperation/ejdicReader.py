# encoding:utf-8
import re

fdic = open("ejdic-hand-utf8.txt", "r", encoding="utf-8")
fw = open("q-list.txt", "wt")

for line in fdic:
    if re.match(r"q[a-z]{3}\s", line):
        fw.write(line)
        print(line.strip())

fdic.close()
