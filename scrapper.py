import requests
import stem
from stem import Signal
from stem.control import Controller
from link_extract import extract_href_links


# Set the proxy to Tor
session = requests.session()
# session.proxies = {"http":"socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate("pass")
        controller.signal(Signal.NEWNYM)


def scrape_example(link):
    # Change the Tor IP address
    # renew_connection()

    # Make a request through Tor
    response = session.get(link)
    print(response.text)

def ahmia_links(keyword):
    response = session.get(f"https://ahmia.fi/search/?q={keyword}")
   
    links=extract_href_links(response.text)
    print(links[20].split(sep='redirect_url=')[1])
    # scrape_example()

ahmia_links('wiki')