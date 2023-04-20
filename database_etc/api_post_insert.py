import requests
import json

url = "http://9.9.9.9:5000/info/post"

payload = json.dumps({
  "sn": "013",
  "cate": "tap",
  "name": "계산기3",
  "content": "계산기 입니다.3",
  "photo": "https://cdn.cln.net/web/api/file/01/1202/19afaafa3.jpg",
  "cnt": "90",
  "status": "1"
})
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

dlst = []
for i in range(111, 10001):
    i = str(i)
    dlst.append({
  "sn": "02"+i,
  "cate": "tap",
  "name": "계산기"+i,
  "content": "계산기 입니다."+i,
  "photo": "https://cdn.cln.net/web/api/file/01/1202/1998aafa3.jpg",
  "cnt": "90"+i,
  "status": "1"
})

for a in dlst:
    payload = json.dumps(a)
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)