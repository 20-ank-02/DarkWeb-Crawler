import stem
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from stem import Signal
from inference import classify_pytorch
from db import put_data,create_csv
from stem.control import Controller
from link_extract import extract_href_links,get_html_text
from link_gen import generate_link

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

count=0
def scrape(link):
    global count
    if count >= 20:
        return 
    count+=1
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
    text=text.replace()
    label=classify_pytorch(text)
    create_csv(text,label)
    put_data(link,label,text)
    links=extract_href_links(response.text)
    for link in links:
        scrape(link)
    
    

def ahmia_links(keyword):
    response = session.get(f"https://ahmia.fi/search/?q={keyword}")
    global count
    links=extract_href_links(response.text)
    i=0
    j=0
    for link in links:
        if j>500:
            print("url count:", i)
            count=0
            scrape(link.split(sep="redirect_url=")[1])
            i+=1
        j+=1
        



ahmia_links('card+fraud')
scrape(generate_link())

collected_onion_links=["muwgjdckwwmhyi7lj73dspumrxmzuzjvujmtmyrhhbjrgswcakobtfad.onion",
"asap2u4sfm3iv4ia77bzrvu4hzozadvgjyhqbdo7ud4grep26o2mvfid.onion",
"darkf52fgy3lwpk3ugngzwp74iw45ib7br2aguww22jgsl54dvojoyid.onion",
"wzabso3y6d3z6iwqqegmkcxc7rgy3j5dzravigp6pvdqi74k6nh4dtyd.onion",
"uvyybhmbvuhxjsaifaskznpll6h4jpaqmqaezfvjbwlmey7v6svzntid.onion",
"dddirectinfv3htc4vl6mied5lpaatora7mmqkcf3sfjrx37fajigmyd.onion",
"vyzjtg3peh3rspo67i55pd644o4vh5ygggqhz25c7w3qwfqwuacifoyd.onion",
]

for link in collected_onion_links:
    scrape(link)