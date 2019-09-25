# import libraries
import requests, re
from bs4 import BeautifulSoup

# specify url
url = 'http://www.espncricinfo.com/icc-champions-trophy-2013/engine/match/566948.html'

# request html
page = requests.get(url)
# print (page.content)

# Parse html using BeautifulSoup, you can use a different parser like lxml if present
soup = BeautifulSoup(page.content, 'html.parser')
win_span = soup.find('span' , class_='cscore_notes_game');
win_text = win_span.text
print(win_text)

# match everything before ' won' in the text
team = re.search('(.*) won', win_text).group(1)
print(team)