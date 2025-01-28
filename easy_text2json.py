with open('中国行政区划代码.txt','r',encoding='utf-8') as file:
    reigen_code : list[str]= file.readlines()
new_reigen_code = []
for line in reigen_code:
    line = line.replace('\n','',1)
    new_reigen_code.append(f'\'{line}\';')
with open('code_reigen.json','w',encoding='utf-8') as f:
    f.writelines(new_reigen_code)