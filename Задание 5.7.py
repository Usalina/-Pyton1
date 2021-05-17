import json

firm_dict={}
list_profit=[]

with open('file_7.txt', 'r', encoding='utf-8') as f:
    count=0
    for line in f:
        firm_list = line.split()
        count+=1
        profit=int(firm_list[2])-int(firm_list[3])
        firm_dict[firm_list[0]] = profit
        list_profit.append(profit)


average_profit={'average_profit': sum(list_profit) / count}
final_list=[firm_dict, average_profit]
print(final_list)


with open('data.json', 'w') as f_obj:
    json.dump(final_list, f_obj)