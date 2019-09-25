# import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen


def fetchThisStock(code):
    # specify the url (YAHOOOO)
    yahoo_page = "https://sg.finance.yahoo.com/quote/" + code + ".si/key-statistics?p=" + code + ".si"

    # query the website and return the html to the variable ‘page’
    page = urlopen(yahoo_page)  # or add .read() behind
    # print(page.read())

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")

    EBITDA = getYahooVar(code, soup, "EBITDA")
    EV = getYahooVar(code, soup, "Enterprise value")
    PSALES = getYahooVar(code, soup, "Price/sales")
    PBOOK = getYahooVar(code, soup, "Price/book")
    ROE = getYahooVar(code, soup, "Return on equity")
    OM = getYahooVar(code, soup, "Operating margin")
    DIV = getYahooVar(code, soup, "Forward annual dividend rate")

    if EBITDA and EV and PSALES and PBOOK and ROE and OM and DIV:
        print (EBITDA + "" + EV + "" + PSALES + "" + PBOOK + "" + ROE + "" + OM + "" + DIV)

    # # specify the url  (INVESTING NOTE)
    # in_page = "https://www.investingnote.com/stocks/SGX:CC3"
    # # query the website and return the html to the variable ‘page’
    # in_page = urlopen(in_page).read()  # or add .read() behind
    # # print(in_page.read())
    #
    # # parse the html using beautiful soup and store in variable `soup`
    # in_soup = BeautifulSoup(in_page, "html.parser")
    #
    # price_span = in_soup.find('strong', class_='stock-price')
    # price_val = price_span.text
    #
    # change_div = in_soup.find('div', class_='stock-change')
    # percent_change =change_div.findChildren()[0].text
    # abs_change =change_div.findChildren()[1].text.strip("()")
    #
    #
    # eps_text = in_soup.find('td', text=re.compile('Trailing EPS.*'))
    # eps_val = eps_text.find_next('td').text
    #
    # beta75_text = in_soup.find('td', text=re.compile('.*Beta - 75 Days.*'))
    # beta75_val = beta75_text.find_next('td').text
    #
    # beta500_text = in_soup.find('td', text=re.compile('.*Beta - 500 Days.*'))
    # beta500_val = beta500_text.find_next('td').text

    # print(beta500_val)


def getYahooVar(code, soup, text):
    ebitda_text = soup.find('span', text=text)
    if ebitda_text is not None:
        ebitda_val = ebitda_text.parent.next_sibling.text
        return ebitda_val
    else:
        print(code + " " + text + " IS NONE -------")
        return False
