import requests
from bs4 import BeautifulSoup
import csv

def find_broken_links(url):
    broken_links = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response was an error

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        for link in links:
            href = link.get('href')
            link_text = link.get_text(strip=True)
            if href and href.startswith('http'):
                try:
                    link_response = requests.get(href)
                    if link_response.status_code >= 400:
                        broken_links.append((url, href, link_text))
                except requests.exceptions.RequestException:
                    broken_links.append((url, href, link_text))
        
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    return broken_links

def save_to_csv(broken_links, filename='broken_links.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Parsed URL', 'Broken Link', 'Link Text'])
        writer.writerows(broken_links)

# Get the URL from the user
url_to_check = input("Enter the URL to check for broken links: ")
broken_links = find_broken_links(url_to_check)

# Save results to CSV
save_to_csv(broken_links)

if broken_links:
    print(f"Broken links found in {url_to_check}. Details saved to 'broken_links.csv'.")
else:
    print(f"No broken links found in {url_to_check}.")