from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
from pyexcel import *

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read().decode("utf-8")


soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table",id = "tableContent")

li_list = ul.find_all("td", "b_r_c")

