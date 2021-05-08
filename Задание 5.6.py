# Уверена, что есть более правильный способ

new_dict={}
with open('file_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line=line.replace(':', '')
        line = line.replace('(л)', '')
        line = line.replace('(пр)', '')
        line = line.replace('(лаб)', '')
        line = line.replace('—', '')
        line = line.replace('.', '')
        one_list=line.split()
        for el in one_list:
            two_list=one_list[1:]
            two_list = list(map(int, two_list))
            lesson = sum(two_list)
            new_dict[one_list[0]] = lesson
print(new_dict)
