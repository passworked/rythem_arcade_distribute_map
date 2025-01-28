import os

# 读取 result 文件夹中的文件名
result_path = './result/'
result_files = {filename[:-4] for filename in os.listdir(result_path) if filename.endswith('.htm')}  # 去掉文件后缀

# 读取 citys1.txt 文件中的城市名称
with open('citys1.txt', 'r', encoding='utf-8') as f:
    city_names = {line.strip() for line in f if line.strip()}  # 去除空行和多余空格

# 找出漏掉的城市
missing_cities = city_names - result_files

# 输出漏掉的城市
if missing_cities:
    print("漏掉的城市文件:")
    for city in missing_cities:
        print(city)
else:
    print("所有城市文件均已存在。")
