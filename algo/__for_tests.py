from collections import defaultdict

N = 1
str = ('123456\n'
       '@@@@@@@@\n'
       'Мама мыла раму\n'
       '@\n'
       'Trololo\n'
       '@@@ @@@\n'
       'Topolya\n'
       '@@')


strings = str.splitlines()

splited = defaultdict(list)
counter = 1

for i, s in enumerate(strings):
    if set(s).issubset('@'):
        counter += 1
    else:
        if counter not in splited.keys():
            splited[counter] = s
        else:
            splited[counter] += '\n' + s

if N in splited.keys():
    print(splited[N])
else:
    print(f"Параграфа {N} не существует")
