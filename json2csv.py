import csv
import json
# 输入的 JSON 数据
data = [
    {"code": "110100", "region_name": "北京市", "count": 107},
    {"code": "120100", "region_name": "天津市", "count": 55},
    # 添加更多数据
]
with open('combined_result_chunithm.json',mode= 'r',encoding= 'utf-8') as f:
    data = json.load(f)
# 输出的 CSV 文件名
output_file = "data.csv"

# 将 JSON 数据写入 CSV 文件
with open(output_file, mode="w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["code", "region_name", "count"])
    writer.writeheader()
    writer.writerows(data)

print(f"数据已成功写入 {output_file}")
