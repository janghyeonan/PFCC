import requests, telegram

response = requests.get("https://www.cien.net/serce/bod/cm")
if response.text.find("1090056187b306443c98bf.gif") != -1:    
    telegram.Bot(token='4835000768:AAGTETWS34tu6R1ORdk4lpb80hO6XLpxc').send_message(chat_id="495484127194", text='심슨 : 정보를 찾았다.')