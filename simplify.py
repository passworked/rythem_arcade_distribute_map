import json

# 读取现有的 arcade_counts.json 文件
with open('arcade_counts.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 过滤和简化结果
filtered_dict = {key[:4]: value for key, value in data.items() if value != 3060}

# 将结果保存回 arcade_counts.json 文件
with open('arcade_counts.json', 'w', encoding='utf-8') as json_file:
    json.dump(filtered_dict, json_file, indent=4, ensure_ascii=False)

print("数据结构已更新并保存回 arcade_counts.json")
