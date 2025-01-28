import json

# 读取 arcade_counts.json 文件
with open('arcade_counts.json', 'r', encoding='utf-8') as arcade_file:
    arcade_data = json.load(arcade_file)

# 读取 code_region.json 文件
with open('code_region.json', 'r', encoding='utf-8') as region_file:
    region_data = json.load(region_file)

# 创建一个新的列表来存储结果
result_list = []

# 遍历 arcade_counts.json 中的每个键值对
for code, count in arcade_data.items():
    # 在 code 的尾部删去8个零
    padded_code = code[:-6]

    
    # 查找对应的行政区名称
    region_name = region_data.get(padded_code, None)  # 如果没有匹配到，返回 None
    
    # 将结果以字典形式添加到列表中
    result_list.append({
        "code": padded_code,
        "region_name": region_name,  # 如果没有匹配到，region_name 为 None
        "count": count
    })

# 将结果保存为新的 JSON 文件
with open('combined_result_chunithm.json', 'w', encoding='utf-8') as output_file:
    json.dump(result_list, output_file, indent=4, ensure_ascii=False)

print("数据已成功结合并保存为 combined_result.json")
