# import libraries
import re

from bs4 import BeautifulSoup
from urllib.request import urlopen


def fetchThisStock(code):
    #  ----------------          Yahoo        ------------
    # specify the url (YAHOOOO)
    yahoo_url = "https://sg.finance.yahoo.com/quote/" + code + ".si/key-statistics?p=" + code + ".si"

    # query the website and return the html to the variable ‘page’
    page = urlopen(yahoo_url)  # or add .read() behind
    # print(page.read())

    soup = BeautifulSoup(page, "html.parser")

    EBITDA = findNextSibling(code, soup, "EBITDA")
    EV = findNextSibling(code, soup, "Enterprise value")
    PSALES = findNextSibling(code, soup, "Price/sales")
    PBOOK = findNextSibling(code, soup, "Price/book")
    ROE = findNextSibling(code, soup, "Return on equity")
    OM = findNextSibling(code, soup, "Operating margin")
    DIV = findNextSibling(code, soup, "Forward annual dividend rate")

    if EBITDA and EV and PSALES and PBOOK and ROE and OM and DIV:
        print (EBITDA + "" + EV + "" + PSALES + "" + PBOOK + "" + ROE + "" + OM + "" + DIV)

    #  ----------------          Yahoo        ------------

    #  ----------------          Investingnote        ------------
    # specify the url  (INVESTING NOTE)
    in_url = "https://www.investingnote.com/stocks/SGX:" + code
    # query the website and return the html to the variable ‘page’
    in_page = urlopen(in_url).read()
    # print(in_page)

    in_soup = BeautifulSoup(in_page, "html.parser")

    price_span = in_soup.find('strong', class_='stock-price')
    PRICE = price_span.text

    change_div = in_soup.find('div', class_='stock-change')
    PERCENT_CHANGE = change_div.findChildren()[0].text
    PRICE_CHANGE = change_div.findChildren()[1].text.strip("()")

    eps_text = in_soup.find('td', text=re.compile('[Trailing EPS.*]|[Trailing EPU.*]'))
    EPS = eps_text.find_next('td').text

    beta75_text = in_soup.find('td', text=re.compile('.*Beta - 75 Days.*'))
    BETA75 = beta75_text.find_next('td').text

    beta500_text = in_soup.find('td', text=re.compile('.*Beta - 500 Days.*'))
    BETA500 = beta500_text.find_next('td').text

    if PRICE and PERCENT_CHANGE and PRICE_CHANGE and EPS and BETA75 and BETA500:
        print (PRICE + "" + PERCENT_CHANGE + "" + PRICE_CHANGE + "" + EPS + "" + BETA75 + "" + BETA500)

    #  ----------------          Investingnote        ------------


def findNextSibling(code, soup, text):
    ebitda_text = soup.find('span', text=text)
    if ebitda_text is not None:
        ebitda_val = ebitda_text.parent.next_sibling.text
        return ebitda_val
    else:
        print(code + " " + text + " IS NONE -------")
        return False
