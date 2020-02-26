from selenium import webdriver

print ("Hello! Welcome to the Craigslist Job Hunter.")
driver = input("Do you use Firefox or Chrome?: ").lower()

while True:
    if driver == 'chrome':
        Driver = webdriver.Chrome()
        break
    elif driver == 'firefox':
        Driver = webdriver.Firefox()
        break
    driver = input("I'm sorry, I didn't understand, do you use Firefox or Chrome?: ")

#Queries
queries = ['code', 'programmer']

#Login
email = input("Enter your e-mail: ")
password = input("Enter your password: ")

payload = {'#inputEmailHandle': email, '#inputPassword': password}
Driver.get('https://accounts.craigslist.org/login')

for el in payload:
    Driver.find_element_by_css_selector(el).send_keys(payload[el])

Driver.find_element_by_css_selector('#login').click()

#Scrape
Driver.get('https://www.craigslist.org/about/sites?lang=en&cc=gb#US')

usDiv = Driver.find_elements_by_css_selector('h1 + div')[0]

usLinks = []
for a in usDiv.find_elements_by_css_selector('a'):
    href = a.get_attribute('href')
    state = href.split('.')[0]
    for query in queries:
        realHref = state + '.craigslist.org/search/crg?query=' + query + '&is_paid=all&lang=en&cc=gb'
        usLinks.append(realHref)

for href in usLinks:
    Driver.get(href)
    a = Driver.find_element_by_css_selector('a.saveme')
    Driver.get(a.get_attribute('href'))
    Driver.find_element_by_css_selector('button').click()
