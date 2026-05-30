#В исходном текстовом файле (radio_stations.txt) найти все домены из URL-адресов (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio домен выделен полужирным)

import re

with open('radio_stations.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

domens = set()

for line in lines:
    reg = re.search('http://([^:/\s]+)', line)
    if reg:
        domen = reg.group(1) 
        domens.add(domen)

print("Найденные домены:")
for domen in domens:
    print(domen)