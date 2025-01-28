import requests
from fake_useragent import UserAgent

# 设置要请求的 URL
url = 'https://map.bemanicn.com/games/3?city=110100000000'  # 替换为你想要请求的 URL
ua = UserAgent()
headers = {
    'User-Agent': ua.chrome
}
try:
    # 发送 GET 请求
    response = requests.get(url,headers)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 打印响应内容
        print('请求成功，内容如下：')
        print(response.text)  # 打印网页的 HTML 内容
        with open('CHUNITHM_1101.htm','w',encoding='utf-8') as f:
            f.write(response.text)
    else:
        print(f'请求失败，状态码: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'请求过程中发生错误: {e}')
