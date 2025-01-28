with open('citys.txt','r',encoding='utf-8') as f:
    citys = f.readlines()
citys =list(set(citys))
citys.sort()
print(citys[0:5])
with open('citys1.txt','w',encoding='utf-8') as f:
    f.writelines(citys)