## 测试序列化

import json

obj = {"name": "123", "password": '123456'}
jsonData = json.dumps(obj)
print(jsonData)
