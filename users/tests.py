import requests
import json

url = 'http://127.0.0.1:8000/login'
# 添加请求头
headers = {
"Content-Type": "application/json;charset=utf-8",
}
result = requests.get(url, headers=headers).text
print(json.loads(result))