from bs4 import BeautifulSoup
# import requests

def extract_href_links(html_content):
    links = []
    soup = BeautifulSoup(html_content, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    # print(soup.get_text()) #returns all the text
    return links

def get_html_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()
    
