import os
import io

work_dir = "path/to/workdir"   #doesnt really matter

for index in range(1, 800): #e.g: 1.txt - 800.txt
    name = "{index}.txt".format(index=index)
    path = os.path.join('/Users/browny/Documents/pwned/user/', name)   #directroy
    with io.open(path, mode="r", encoding="utf-8") as fd:
        for line in fd:
            if "crandell" in line: print(line)   #keyphrase
        fd.close()
