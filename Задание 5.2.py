
with open('file_2.txt') as f:
    line_count=0
    for line in f:
        line_count += 1
print(f'Кол-во строк', line_count)

with open('file_2.txt') as f:
    for lines in f:
        new_line=(lines.split())
        print(f'Строка:', new_line)
        print(f'Кол-во слов', len(new_line))

f.close()





