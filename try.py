with open('Array.txt') as myfile:
    for line in myfile.readlines():
        if line.strip() != '[[' and line.strip() != ']]' and line.strip():
            print (line)