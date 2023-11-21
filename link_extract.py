from bs4 import BeautifulSoup
# import requests

def extract_href_links(html_content):
    links = []
    soup = BeautifulSoup(html_content, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    # print(soup.get_text()) #returns all the text
    return links

# # Example usage:
# url = 'https://example.com'
# response = requests.get(url)
# html_content = response.text

# href_links = extract_href_links(html_content)

# print("Extracted HREF links:")
# for link in href_links:
#     print(link)
