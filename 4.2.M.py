string = 'яндеКс Яндекс янДекс использует Python во многих проектах'
print(sorted(string.split(), key=lambda line: (len(line), line.lower())))