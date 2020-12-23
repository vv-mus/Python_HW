from re import findall


subj = {}
with open('Data\\5.6.txt', 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        total = 0
        hours = findall(r'\d+', line)
        for el in hours:
            total += int(el)
        subj[line.split()[0]] = total
    print(subj)
