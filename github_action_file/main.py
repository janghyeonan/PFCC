import requests
import datetime
import telegram
from bs4 import BeautifulSoup
import sys
import re

domain = "https://www.cln.net/"
url = domain + "serce/bod/pak"
sort_word = {'이', '에', '가', '의', '와', '는', '은', '에게', '라는', '과', '를', '에서', '을'}
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
word_lst =[]
for j, k, l in zip([i.get_text().replace('\t',"").replace('\n',"") for i in soup.select('.subject_fixed')], [a.get_text().replace('\t',"").replace('\n',"") for a in soup.select('.timestamp')],[domain[:-1]+o.attrs["href"] for o in soup.select(".list_subject")]):
    lst = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', j).replace("  ","")
    print(k+" "+lst +" "+l)    
    for j in lst.split(" "):
        word_lst.append(j)        
    if "sale" in j:
        telegram.Bot(token=sys.argv[1]).send_message(chat_id=sys.argv[2], text=l)

sset ={}
for i in word_lst:
    if i in sset:
        sset[i] += 1
    else:
        sset[i] = 1

sorted_dict = sorted(sset.items(), reverse=True, key=lambda x: x[1])
content_t = ''.join([i[0]+str(i[1])+', ' for i in sorted_dict[0:11]])
print(content_t)