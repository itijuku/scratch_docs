import requests
import numpy as np
import matplotlib.pyplot as plt
import time

url = 'https://api.scratch.mit.edu/explore/projects?limit=16&offset=0&language=ja&mode=trending&q=*'

response = requests.get(url)
assert (response.status_code == 200 and response.text),f"読み込み失敗 status_code:{response}"

tag_name = ["#all","#animations","#art","#games","#music","#stories","#tutorials"]

in_tag_data = []
tag_number = [0,0,0,0,0,0,0]
for i in range(len(response.json())):
    tag_data = []
    for tag in tag_name:
        if tag in response.json()[i]["description"] or tag in response.json()[i]["instructions"]:
            tag_data.append("1")
            tag_number[tag_name.index(tag)] = tag_number[tag_name.index(tag)] + 1
        else:
            tag_data.append("0")
    in_tag_data.append(tag_data)
    
with open(f"response/data/{time.strftime('%Y-%m-%d-%H-%M-%S')}","a") as data:
    data.write(str(tag_number))

plt.pie(tag_number, labels=tag_name,autopct="%1.1f%%")
plt.show()
