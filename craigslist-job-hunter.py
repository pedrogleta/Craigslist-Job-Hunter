from selenium import webdriver

chrome = webdriver.Chrome()

#Queries
queries = ['illustration', 'illustrator']

#Login
payload = {'#inputEmailHandle': '', '#inputPassword': ''}
chrome.get('https://accounts.craigslist.org/login')

for el in payload:
    chrome.find_element_by_css_selector(el).send_keys(payload[el])

chrome.find_element_by_css_selector('#login').click()

#Scrape
chrome.get('https://www.craigslist.org/about/sites?lang=en&cc=gb#US')

usDiv = chrome.find_elements_by_css_selector('h1 + div')[0]

usLinks = []
for a in usDiv.find_elements_by_css_selector('a'):
    href = a.get_attribute('href')
    state = href.split('.')[0]
    for query in queries:
        realHref = state + '.craigslist.org/search/crg?query=' + query + '&is_paid=all&lang=en&cc=gb'
        usLinks.append(realHref)

for href in usLinks:
    chrome.get(href)
    a = chrome.find_element_by_css_selector('a.saveme')
    chrome.get(a.get_attribute('href'))
    chrome.find_element_by_css_selector('button').click()
