import json
from pprint import pprint

with open("C:\\Test\\data.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
records[1]["group_number"] = 123
with open("../Test/data2.json", "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)
