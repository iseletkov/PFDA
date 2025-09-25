from sys import stdin
import json

lines = stdin.readlines()

file_in_name = lines[0].rstrip("\n")

with open(file_in_name, encoding="UTF-8") as file_in:
    dict1 = json.load(file_in)
    
for i in range(1, len(lines)):
    pairlist = lines[i].rstrip("\n").split(" == ")

    dict1[pairlist[0]] = pairlist[1]

with open(file_in_name, "w", encoding="UTF-8") as file_out:
    json.dump(dict1, file_out, ensure_ascii=False, indent=4)



