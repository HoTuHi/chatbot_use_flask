import requests
from bs4 import BeautifulSoup


def getfuntion(Usetext):
    te = requests.get(Usetext)
    return te.text

getfuntion("https://code.junookyo.xyz/api/ncov-moh/data.json?fbclid=IwAR0REJuqmciGS2LifyoSt0b4olDPfWeIJ5fq3stcclqJnI1GFVPQKwEIB20")
