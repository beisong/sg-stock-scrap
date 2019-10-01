# import libraries
import re
import time
import logging

from bs4 import BeautifulSoup
from urllib.request import urlopen

logger = logging.getLogger(__name__)
showElapsed = False


def convertUnits(string):
    # https://stackoverflow.com/questions/51611027/how-to-convert-strings-with-billion-or-million-abbreviation-into-integers-in-a-l
    m = {'k': 3, 'm': 6, 'b': 9, 't': 12, 'K': 3, 'M': 6, 'B': 9, 'T': 12}
    return int(float(string[:-1]) * 10 ** m[string[-1]])


def fetchThisStock(code):
    logger.info("FETCHING :" + code)
    #  ----------------          Yahoo        ------------
    # specify the url (YAHOOOO)
    if showElapsed:
        yahoo_start = time.time()
    yahoo_url = "https://sg.finance.yahoo.com/quote/" + code + ".si/key-statistics?p=" + code + ".si"

    # query the website and return the html to the variable ‘page’
    page = urlopen(yahoo_url)  # or add .read() behind
    # print(page.read())

    rawsoup = BeautifulSoup(page, "html.parser")
    soup = rawsoup.find('div', class_='YDC-Col1')

    EBITDA = findNextSibling_yahoo(code, soup, "EBITDA")
    if EBITDA is not False and EBITDA != "N/A":
        EBITDA = convertUnits(EBITDA)

    EV = findNextSibling_yahoo(code, soup, "Enterprise value")
    if EV is not False and EV != "N/A":
        EV = convertUnits(EV)

    PSALES = findNextSibling_yahoo(code, soup, "Price/sales")
    PBOOK = findNextSibling_yahoo(code, soup, "Price/book")
    ROE = findNextSibling_yahoo(code, soup, "Return on equity")
    OM = findNextSibling_yahoo(code, soup, "Operating margin")
    DIV = findNextSibling_yahoo(code, soup, "Forward annual dividend rate")

    if EBITDA and EV and PSALES and PBOOK and ROE and OM and DIV:
        # print (EBITDA + "" + EV + "" + PSALES + "" + PBOOK + "" + ROE + "" + OM + "" + DIV)
        pass
    else:
        logger.error("YAHOO Values Missing for :" + code)
        return

    if showElapsed:
        yahoo_end = time.time()
        print ("YAHOO ELAPSED : %f " % (yahoo_end - yahoo_start))

    #  ----------------          Yahoo        ------------

    #  ----------------          Investingnote        ------------
    if showElapsed:
        in_start = time.time()

    # specify the url  (INVESTING NOTE)
    in_url = "https://www.investingnote.com/stocks/SGX:" + code
    # query the website and return the html to the variable ‘page’
    in_page = urlopen(in_url).read()
    # print(in_page)

    in_soup = BeautifulSoup(in_page, "html.parser")

    # nameheader = in_soup.find('h4', class_='stock-name')
    # fullname = nameheader.a.span.text
    # STOCKNAME = re.sub(r'\(.*\)', '', fullname).rstrip()  # remove stock code in bracket eg.  (SGX: AZG)

    price_span = in_soup.find('strong', class_='stock-price')
    PRICE = price_span.text

    change_div = in_soup.find('div', class_='stock-change')
    PERCENT_CHANGE = change_div.findChildren()[0].text
    PRICE_CHANGE = change_div.findChildren()[1].text.strip("()")

    eps_text = in_soup.find('td', text=re.compile('[Trailing EPS.*]|[Trailing EPU.*]'))
    EPS = getNextSiblingText_IN(eps_text, in_soup, "EPS")
    # EPS = eps_text.find_next('td').text

    beta75_text = in_soup.find('td', text=re.compile('.*Beta - 75 Days.*'))
    BETA75 = getNextSiblingText_IN(beta75_text, in_soup, "75Beta")
    # BETA75 = beta75_text.find_next('td').text

    beta500_text = in_soup.find('td', text=re.compile('.*Beta - 500 Days.*'))
    BETA500 = getNextSiblingText_IN(beta500_text, in_soup, "500Beta")
    # BETA500 = beta500_text.find_next('td').text

    if PRICE and PERCENT_CHANGE and PRICE_CHANGE and EPS and BETA75 and BETA500:
        # print ( PRICE + "" + PERCENT_CHANGE + "" + PRICE_CHANGE + "" + EPS + "" + BETA75 + "" + BETA500)
        pass
    else:
        logger.error("INote Values Missing for :" + code)
        return

    if showElapsed:
        in_end = time.time()
        print ("INote  ELAPSED : %f " % (in_end - in_start))
    #  ----------------          Investingnote        ------------

    stockData = [PRICE, PRICE_CHANGE, PERCENT_CHANGE, EPS, BETA75, BETA500, EBITDA, EV, PSALES, PBOOK,
                 ROE, OM, DIV]
    return stockData


def findNextSibling_yahoo(code, soup, text):
    text_to_find = soup.find('span', text=text)
    if text_to_find is not None:
        val = text_to_find.parent.next_sibling.text
        return val
    else:
        logger.warning(code + " " + text + "           ------------- NOT AVAILABLE ------------- ")
        print(code + " " + text + "           ------------- NOT AVAILABLE ------------- ")
        return False


def getNextSiblingText_IN(element, soup, indicator):
    if element is not None:
        return element.find_next('td').text
    else:
        logger.warning(indicator + "           ------------- NOT AVAILABLE ------------- ")
        print(indicator + "           ------------- NOT AVAILABLE ------------- ")
        return False
