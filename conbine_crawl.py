import os
import re
import json
import requests
from fake_useragent import UserAgent

# 定义正则表达式
regex_arcade_count = r'arcade_count&quot;:&quot;(\d+)&quot;'
regex_zero_count = r'arcade_count&quot;:0'
r1 = re.compile(regex_arcade_count)
r2 = re.compile(regex_zero_count)

# 初始化
ua = UserAgent()
headers = {
    'User-Agent': ua.chrome
}
result_dict = {}

# 读取城市列表
with open('citys1.txt', 'r', encoding='utf-8') as f:
    citys_list = f.read().split('\n')
citys_list = [city for city in citys_list if city != '']

# 请求并保存结果
htm_files_path = './result/'  # 存放 .htm 文件的目录
os.makedirs(htm_files_path, exist_ok=True)  # 创建目录

for city in citys_list:
    url = f'https://map.bemanicn.com/games/3?city={city}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(os.path.join(htm_files_path, f'{city}.htm'), 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            # 提取 arcade_count
            match = r1.search(response.text)
            arcade_count = int(match.group(1)) if match else 0

            if r2.search(response.text):
                arcade_count = 0

            result_dict[city] = arcade_count
            print(f'{city[:4]} 请求成功，一共有 {arcade_count} 台中二')
        else:
            print(f'{city[:4]} 请求失败，状态码: {response.status_code}')
            result_dict[city] = 'error'
    except requests.exceptions.RequestException as e:
        print(f'请求过程中发生错误: {e}')
        result_dict[city] = 'error'

# 解析本地保存的 .htm 文件
for filename in os.listdir(htm_files_path):
    if filename.endswith('.htm'):
        city_name = filename[:-4]  # 去掉文件后缀以获取城市名称
        if city_name not in result_dict or result_dict[city_name] == 'error':
            with open(os.path.join(htm_files_path, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                match = r1.search(content)
                arcade_count = int(match.group(1)) if match else 0

                if r2.search(content):
                    arcade_count = 0

                result_dict[city_name] = arcade_count

# 保存结果为 JSON 文件
with open('arcade_counts.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_dict, json_file, indent=4, ensure_ascii=False)

print("数据已生成并保存为 arcade_counts.json")