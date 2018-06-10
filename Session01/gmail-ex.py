from gmail import *
from random import choice

gmail =GMail('annedev165@gmail.com','Nga16051992')

html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc Lập - Tự Do - Hạnh Ph&uacute;c</p>
<p>&nbsp;</p>
<h1 style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></h1>
<p>&nbsp;</p>
<p>K&iacute;nh gửi: <strong>C&ocirc; gi&aacute;o chủ nhiệm lớp 12A2</strong></p>
<p>T&ecirc;n em l&agrave;: Nga Nguyễn</p>
<p>H&ocirc;m nay, em viết đơn để mong Cô cho phép em nghỉ học vì {{sickness}}. Em xin hứa sẽ học b&agrave;i v&agrave; ch&eacute;p b&agrave;i đầy đủ trước khi đến lớp.&nbsp;</p>
<p>Xia xia ni</p>
<p>&nbsp;</p>
<p style="text-align: right;">&nbsp;</p>
<p style="text-align: right;">Ký tên</p>
<p style="text-align: right;"><strong>Nga Nguyễn</strong></p>
"""

# placeholder
reasons = ["về quê","đau bụng","mệt quá"]
replace = choice(reasons)

html_content_to_send = html_content.replace("{{sickness}}",replace)


msg = Message('NgaNguyen','20130075@student.hust.edu.vn',html=html_content_to_send)
gmail.send(msg)