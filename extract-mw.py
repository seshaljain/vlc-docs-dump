from bs4 import BeautifulSoup

with open('wikivideolanorg-20200528-wikidump/wikivideolanorg-20200528-current.xml', 'r') as f:
    soup = BeautifulSoup(f)
    
    for page in soup.find_all('page'):
        page_name = page.find('title').get_text()
        file_name = 'mediawiki/' + page_name.replace(" ", "_").replace(".", "-").replace("*", "-").replace(":", "-").replace("/", "--") + '.mediawiki'
        mw_data = PAGE.find('text').get_text()
        with open (file_name, 'w') as E:
            E.write(mw_data)
        # break                   # to try on single file


