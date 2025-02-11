import requests
from bs4 import BeautifulSoup

def scrape_property(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').get_text(strip=True)
        price = soup.find('span', class_='price').get_text(strip=True)
        return {'title': title, 'price': price}
    else:
        return None

if __name__ == "__main__":
    property_url = "https://example.com/property"
    data = scrape_property(property_url)
    if data:
        print("Property Data:", data)
    else:
        print("Failed to fetch property data.")
