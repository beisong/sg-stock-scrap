# importing libraries
from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
page = urllib.request.urlopen(url) # conntect to website
#can import this instead
# from urllib.request import urlopen
# ten can use urlopen directly

try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")

soup = BeautifulSoup(page, 'html.parser')
# print(soup)

# When we inspected the website we saw that every list item in the content section has a class that starts with tocsection- and we can us BeautifulSoup’s find_all method to find all list items with that class.
regex = re.compile('^tocsection-')
content_lis = soup.find_all('li', attrs={'class': regex})
#print(content_lis)


# To get the raw text we can loop through the array and call the getText method on each list item.
content = []
for li in content_lis:
    content.append(li.getText().split('\n')[0])
# print(content)


# To get the data from the “see also” section, we use the find method to get the div containing the list items, and then use find_all to get an array of list items.
see_also_section = soup.find('div', attrs={'class': 'div-col columns column-width'})
see_also_soup =  see_also_section.find_all('li')
print(see_also_soup)


# To extract the hrefs and the text a loop in combination with the find method can be used.
see_also = []
for li in see_also_soup:
    a_tag = li.find('a', href=True, attrs={'title': True})  # find a tags that have a title and a class
    href = a_tag['href']  # get the href attribute
    text = a_tag.getText()  # get the text
    see_also.append([href, text])  # append to array
print(see_also)



# SAVING DATA
# with open('content.txt', 'w') as f:
#     for i in content:
#         f.write(i+"\n")
#
# with open('see_also.csv', 'w') as f:
#     for i in see_also:
#         f.write(",".join(i) + "\n")