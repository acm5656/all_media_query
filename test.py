import re
from bs4 import BeautifulSoup
html ='<p>https://www.youtube.com/watch?v=aoXWi3TZfaE&nbsp;<br></p><p>更多精彩内容访问GuitarCIA.com或关注“吉他情报局”微博和微信公众号与我们互动</p><p><br></p>'
# pattern = re.compile(r'<[^>]+>',re.S)
# result = pattern.sub('', html)
# print(result)

soup = BeautifulSoup(html,'html.parser')
print(soup.get_text())