from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
url = "http://dantri.com.vn"
# 1. Download web page
# #1.1 Create a connection
conn = urlopen(url)
# #1.2 Read
data = conn.read()
# #1.3 Decode
html_content = data.decode('utf-8')
print(html_content)

# Cách nhanh hơn :
# html = urlopen("http://dantri.com.vn/").read().decode('utf-8')


# Save html_content to file
# urlretrieve(url, "dantri.html")

# f = open("dantri1.html", "wb")
# f.write(html_content)
# f.close()



#2. Extract ROI (region of interest)
#html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")

# print(soup.prettify())

ul = soup.find("ul","ul1 ulnew")
# print(ul.prettify())

li_list = ul.find_all("li")
# print(li_list.prettify())

for li in li_list:
    # print(li.prettify())
    # print("*" *20)
    # # h4 = li.find("h4")
    # # a = h4.find("a")
    # h4 = li.h4
    # a = h4.a
    a = li.h4.a
    # print(a.prettify())

    print(url + a['href'])
    break

#3. Extract info