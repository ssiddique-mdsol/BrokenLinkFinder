import requests
from bs4 import BeautifulSoup
import csv
import xml.etree.ElementTree as ET

def get_urls_from_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        sitemap = ET.fromstring(response.content)
        urls = [url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for url in sitemap]
        
        return urls
    except requests.exceptions.RequestException as e:
        print(f"Error accessing sitemap {sitemap_url}: {e}")
        return []

def find_broken_links(url):
    broken_links = []
    try:
        response = requests.get(url)
        response.raise_for_status()

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

# Get the sitemap URL from the user
sitemap_url = input("Enter the sitemap URL: ")
urls = get_urls_from_sitemap(sitemap_url)

all_broken_links = []
for url in urls:
    broken_links = find_broken_links(url)
    all_broken_links.extend(broken_links)

# Save results to CSV
save_to_csv(all_broken_links)

if all_broken_links:
    print(f"Broken links found. Details saved to 'broken_links.csv'.")
else:
    print(f"No broken links found.")