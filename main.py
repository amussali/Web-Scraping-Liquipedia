from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://liquipedia.net/dota2/Miracle-').text
soup = BeautifulSoup(html_text, 'lxml')
player_info = soup.find("div", class_ = "fo-nttax-infobox")
divs = player_info.find_all("div")
headers = []
data = []
for div in divs:
    single_header = div.find("div", class_ = "infobox-cell-2 infobox-description")
    single_data = div.find("div", {"style": "width:50%"})
    
    if single_header != None:
        headers.append(single_header)
    if single_data != None:
        data.append(single_data)

print(headers)
print()
print(data)