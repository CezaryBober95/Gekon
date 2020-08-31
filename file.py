import re
with open("Geko2.txt") as myfile:
    file = open("macierze.txt", "w+")
    for line in myfile.readlines():
        if line.strip().startswith('['):
            matrix = re.sub(" +", " ", line)
            matrix1 = (re.sub(' ', ',', matrix)).strip()
            matrix2 = re.sub(",]", "]", matrix1)
            matrix3 = re.sub(",\[", '[', matrix2)
            matrix4 = re.sub("]", "],\n", matrix3)
            matrix5 = re.sub("],\n],", "]]\n", matrix4)
            matrix6 = re.sub("\[\[", "[[", matrix5)
            matrix7 = re.sub("]", "", matrix6)
            matrix8 = re.sub("\[", "", matrix7)
            matrix9 = re.sub(",", " ", matrix8)
            print(matrix9)
            file.write(matrix9)

myfile.close()