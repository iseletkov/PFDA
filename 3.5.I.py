import re

file_in_name = input()
file_out_name = input()

with open(file_in_name, encoding="UTF-8") as file_in:
    with open(file_out_name, "w", encoding="UTF-8") as file_out:
        for line in file_in:
            # line = re.sub(r' +', ' ', line)  # удаляет повторные символы
            line = re.sub(r'\t', '', line) 
            line = re.sub(r'\s+\n', '\n', line) 
            line = re.sub(r'\n\s+', '\n', line) 
            line = re.sub(r'\n+', '\n', line) 
            line = re.sub(r' +', ' ', line) 
            
            # line = line.lstrip()
            # line = line.rstrip()
            line = line.strip(" ")
            if len(line)==0:
                continue
            if line=="\n":
                continue

            file_out.write(line)

#  input_1.txt
#  output_1.txt