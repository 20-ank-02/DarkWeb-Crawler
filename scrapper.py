import stem
import requests
from stem import Signal
from inference import classify
from db import put_data,create_csv
from stem.control import Controller
from link_extract import extract_href_links,get_html_text


# Set the proxy to Tor
session = requests.session()
# session.proxies = {"http":"socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate("pass")
        controller.signal(Signal.NEWNYM)


def scrape(link):

def scrape(link):
    # Change the Tor IP address
    # renew_connection()

    # Make a request through Tor
    response = session.get(link)
    
    text=get_html_text(response.text)
    # label=classify(text)
    put_data(link,"label",text)
    links=extract_href_links(response.text)
    for link in links:
        scrape(link)
    
    

def ahmia_links(keyword):
    response = session.get(f"https://ahmia.fi/search/?q={keyword}")
   
    links=extract_href_links(response.text)
    i=0
    for link in links:
        if i>9:
            scrape(link.split(sep="redirect_url=")[1])
        i+=1


ahmia_links('card')