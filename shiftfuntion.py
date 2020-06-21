import requests
import json

resp = open('city.json', 'r', encoding='utf-8')
data_file = json.load(resp)
city_data = data_file['data']


def corona(usertext):
    urlVN = "https://ncovi.huynhhieu.com/api.php?code=external"
    u = requests.get(urlVN)
    x = u.text
    # print(x)
    res = json.loads(x)
    data = res['data']

    # print(data[0]['total_cases'])
    # print(res)
    # usertext = "Russia"
    for ilus in data:
        if ilus['country'] == usertext:
            text = "Quốc gia   : " + ilus['country'] + \
                "\n" + " - Ca nhiễm  : " + \
                ilus['cases'] + "   Chết      : " + ilus['deaths']
            return text
    return "NHAP LAI DI MAY"


def getsub(usertext):
    url = "http://numbersapi.com/" + usertext
    u = requests.get(url)
    x = u.text
    if "Cannot" in x:
        x = "NHAP LAI DI MAY"
    return x


def gettemp(usertext):
    text = usertext.split(' ', 1)[1]
    # text = "Tỉnh " + text
    # print(text)
    for ilus in city_data:
        if ilus['name'] == text:
            haha = ilus['coord']
            # print(haha['lon'])
            urltemp = "http://api.openweathermap.org/data/2.5/weather?lat=" + \
                str(haha['lat']) + "&lon=" + str(haha['lon']) + \
                "&units=metric&appid=e0b3d8ec6bafb06c5161739549742e7a"
            x = requests.get(urltemp)
            x = x.text

            # x = open('x.json', 'r', encoding='utf-8')
            # x =x.read()
            res = json.loads(x)
            weather = res['weather']
            main = res['main']
            text = "thời tiết " + text + "; " + weather[0]['main'] + "; " + "nhiệt độ :  " + str(main['temp_min']) + "°C /" + str(main['temp_max']) + "°C  ; " + "cảm giác như : " + str(main['feels_like']) +"°C"
            return text
    return "NHAP LAI DI MAY"
# print(gettemp("temp Nghệ An"))


# xas = open('x.json')
# xas = xas.read()
# res = json.loads(xas)
# weather = res['weather']
# main = res['main']
# text = "thời tiết " + "xxxx" + " <br> " + weather[0]['main'] + " <br> " + "nhiệt độ :  " + str(main['temp_min']) + "/" + str(main['temp_max']) + " <br> " + "cảm giác như : " + str(main['feels_like'])
# print(text)
