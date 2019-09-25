#!/usr/bin/python3
import requests                # Include HTTP Requests module
from bs4 import BeautifulSoup  # Include BS web scraping module


url = "https://communityfoundations.ca/find-a-community-foundation/" # Website / URL we will contact
r = requests.get(url)           # Sends HTTP GET Request
print(r.status_code)            # ---> Print HTML status code <---
soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response
print(soup.prettify())          # Prints user-friendly results

# find() Method
# sticker = soup.find('div', id="stickers_btn")  # Use print() for the results
# print(sticker)


### returns the first div on the page
# soup.find('div')
## find the first div with id='welcome_message'
soup.find('div', class_='gm-style-iw-d')
print(soup.children.text)
### finds the respective HTML tag element
# soup.title
# soup.h1
# soup.body.div


### find_all put all of the same type of elements into an array
# soup.find_all('a')      # finds all <a> elements
# soup.find_all('a')[0]   # reference the first <a> element
# soup.find_all('a')[1]   # reference the second <a> element
### loop over array
# for link in soup.find_all('a'):  # iterate over every <a> tag
#     print(link)                  # print it to the screen

### get_text()
# for link in soup.find_all('a'):  # iterate over every <a> tag
#     print(link.get_text())       # print it to the screen

#### get()  eg. get href
# for link in soup.find_all(‘a’):
#     print(link.get(‘href’))