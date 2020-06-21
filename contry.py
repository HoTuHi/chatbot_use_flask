import requests
import json
urlVN = "https://ncovi.huynhhieu.com/api.php?code=external"
u = requests.get(urlVN)
x = u.text
# print(x)
res = json.loads(x)
data = res['data']
# print(data[0]['total_cases'])
# print(res)
print("cập nhật vào : ", res['updated'] + "+0:00 GTM")
print("_____________________")
usertext = "Russia"
for ilus in data:
    if ilus['country'] == usertext:
        print("Quốc gia  : ", ilus['country'])
        print("Ca nhiễm  : ", ilus['cases'])
        if ilus['deaths'] == "":
            ilus['deaths'] = "0"
        print("Chết      : ", ilus['deaths'])
        print("Bình phục : ", ilus['recovered'])
        # print("ca nhiễm mới : ", data[0]['new_cases'])
        print("_____________________")
