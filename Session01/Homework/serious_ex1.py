from gmail import *
from random import choice
import datetime 

html_content = """
<p style="text-align: center;">Cộng H&ograve;a X&atilde; Hội Chủ Nghĩa Việt Nam</p>
<p style="text-align: center;">Độc Lập - Tự Do - Hạnh Ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<h1 style="text-align: center;"><strong>ĐƠN XIN NỘP B&Agrave;I MUỘN</strong></h1>
<p>Th&acirc;n gửi: Dinh Quy</p>
<p>M&igrave;nh viết đơn n&agrave;y mong Qu&yacute; th&ocirc;ng cảm cho m&igrave;nh nộp b&agrave;i muộn vì{{sickness}} n&ecirc;n chưa sắp xếp được thời gian l&agrave;m b&agrave;i tập về nh&agrave;. M&igrave;nh hứa sẽ cố gắng hết sức lần sau :D</p>
<p>&nbsp;</p>
<p style="text-align: right;">K&yacute; t&ecirc;n</p>
<p style="text-align: right;">Nga Nguyễn</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
"""

reasons = ["too busy","sick","too difficult","need more time to figure it out"]
replace = choice(reasons)
html_content_to_send = html_content.replace("{{sickness}}",replace)

now = datetime.datetime.now()
time = now.hour

msg = Message('NgaNguyen','annedev165@gmail.com',html=html_content_to_send)

if time >7:
    gmail.send(msg)
