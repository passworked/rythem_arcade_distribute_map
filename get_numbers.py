import requests
import json
from fake_useragent import UserAgent
from lxml import html
import re

# 创建 User-Agent
ua = UserAgent()
headers = {
    'User-Agent': ua.chrome
}
url = 'https://map.bemanicn.com/games/1?city='

# 从 JSON 文件中读取城市代码
with open('crawl_target.json', 'r', encoding='utf-8') as f:
    code_citys: dict = json.load(f)

# 用于存储结果的字典
results = {}

# 遍历城市代码
for key in code_citys:
    # 跳过特定的城市代码
    if key[-2:-1] == '00' and key[2:-1] != '0000':
        print(key)

        # 构建正确的 URL
        city_code = key + '000000'  # 只使用单个城市代码

        full_url = f'{url}{city_code}'
        print(full_url)
        
        # 发送 GET 请求
        response = requests.get(url=full_url, headers=headers)
    
    # 检查请求是否成功
        if response.status_code == 200:
            # 解析 HTML 内容
            tree = html.fromstring(response.content)
            
            # 提取指定 XPath 的文本
            text_content = tree.xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[1]/text()')
            
            # 将提取的文本合并为一个字符串
            full_text = ''.join(text_content).strip()
            
            # 使用正则表达式提取数字
            match = re.search(r'共(\d+)台', full_text)
            if match:
                number_of_machines = match.group(1)
                results[key] = number_of_machines  # 保存结果到字典
                print(f'城市代码: {key}, 机器数量: {number_of_machines}')
            else:
                print(f'城市代码: {key}, 未找到机器数量信息')
        else:
            print(f'城市代码: {key}, 请求失败，状态码: {response.status_code}')

# 将结果保存到 JSON 文件
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print('结果已保存到 results.json')
