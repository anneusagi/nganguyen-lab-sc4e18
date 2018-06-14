from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from pyexcel import *
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

html_content = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")
sec = soup.find("section","section chart-grid")

list_of_songs = []
li_list = sec.find_all("li")
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1 
}
dl = YoutubeDL(options)

for li in li_list:
    dic_songs = {} 
    h3 = li.h3
    dic_songs["Name"] = h3.string
    h4 = li.h4
    dic_songs["Artist"] = h4.string
    
    list_of_songs.append(dic_songs)
    
    
    download = h3.string + " " + h4.string
    dl.download([download])


save_as(records=list_of_songs, dest_file_name="itunes_top.xlsx")