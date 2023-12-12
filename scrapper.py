import stem
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from stem import Signal
#from inference import classify
from db import put_data,create_csv
from stem.control import Controller
from link_extract import extract_href_links,get_html_text
import time

# Set the proxy to Tor
session = requests.session()

#retry = Retry(connect=3, backoff_factor=0.5)
#adapter = HTTPAdapter(max_retries=retry)
#session.mount('http://', adapter)
#session.mount('https://', adapter)

session.proxies = {"http":"socks5h://localhost:9050", "https": "socks5h://localhost:9050"}


def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate("548390A@")
        controller.signal(Signal.NEWNYM)

# count=0
def scrape(link):
    # global count
    # if count >= 2:
    #     return 
    # count+=1
    # Change the Tor IP address
    renew_connection()

    # print("count: ",count)
    # Make a request through Tor
    try:
        response = session.get(link)
    except Exception as errorLink:
        print("Url error for: ",str(errorLink))
        return 
    text=get_html_text(response.text)
    
    # label=classify(text)
    create_csv(text,"card-fraud")
    #links=extract_href_links(response.text)
    #for link in links:
        #scrape(link)
    
    

def ahmia_links(keyword):
    response = session.get(f"https://ahmia.fi/search/?q={keyword}")
    # global count
    links=extract_href_links(response.text)
    i=0
    j=0
    for link in links:
        if j>500:
            print("url count:", i)
            # count=0
            scrape(link.split(sep="redirect_url=")[1])
            i+=1
        j+=1
        



ahmia_links('card+fraud')