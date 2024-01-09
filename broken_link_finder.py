import requests
from bs4 import BeautifulSoup

def find_broken_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response was an error

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        broken_links = []
        for link in links:
            print(link)
            href = link.get('href')
            if href and href.startswith('http'):
                try:
                    link_response = requests.get(href)
                    if link_response.status_code >= 400:
                        broken_links.append(href)
                except requests.exceptions.RequestException:
                    broken_links.append(href)
        
        return broken_links

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

# Get the URL from the user
url_to_check = input("Enter the URL to check for broken links: ")
broken_links = find_broken_links(url_to_check)
print(f"Broken links in {url_to_check}:")
for link in broken_links:
    print(link)