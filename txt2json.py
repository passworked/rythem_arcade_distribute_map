import json
with open('中国行政区划代码.txt','r',encoding='utf-8') as file:
    reigen_code : list[str]= file.readlines()
province : list[str] = []
city : list[str]= []
counties : list[str] = []
json_file : list[str] = [] 
def get_name(line:str):
    code_and_reigen=line.split('\t')
    return {'code':code_and_reigen[0],
            'name':code_and_reigen[1]}
with open('reigen_code.json','w',encoding='utf-8') as reigen_code_json:
    for line in reigen_code:
        if line[2:5] == '0000':
            province : list[str] = []
            city : list[str]= []
            counties : list[str] = []
            province.append(get_name(line))
        elif line[4:5] == '00':
            city : list[str]= []
            counties : list[str] = []
            city.append(get_name(line))
        else:
            counties.append(get_name(line))