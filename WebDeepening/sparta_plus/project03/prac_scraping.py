import requests
from bs4 import BeautifulSoup


url = "https://www.melon.com/chart/day/index.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

req = data.text
soup = BeautifulSoup(req, 'html.parser')

songs = soup.select("#frm > div > table > tbody > tr")
print(len(songs))

for song in songs:
    title = song.select_one("td > div > div.wrap_song_info > div.rank01 > span > a").text
    artist = song.select_one("td > div > div.wrap_song_info > div.rank02 > span > a").text
    likes = song.select_one("td > div > button.like > span.cnt").text
    print(title, artist, likes)