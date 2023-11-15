import requests
import stem
from stem import Signal
from stem.control import Controller

# Set the proxy to Tor
session = requests.session()
session.proxies = {"http":"socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate("pass")
        controller.signal(Signal.NEWNYM)

# Example usage
def scrape_example():
    # Change the Tor IP address
    renew_connection()

    # Make a request through Tor
    response = session.get("http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion")
    print(response.text)

if __name__ == "__main__":
    scrape_example()
