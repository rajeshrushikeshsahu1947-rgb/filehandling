import requests
from bs4 import BeautifulSoup
import csv

URL = "http://books.toscrape.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

products_data = []

# Each book is inside an article tag with class 'product_pod'
product_containers = soup.find_all('article', class_='product_pod')

for container in product_containers:
    name = container.h3.a['title']
    price = container.find('p', class_='price_color').text.strip()
    rating = container.p['class'][1]  # rating is stored as a class name like 'Three'

    products_data.append({'Name': name, 'Price': price, 'Rating': rating})

# Save to CSV
csv_file = r"C:\Users\Rajesh\Downloads\ecommerce_products.csv"
headers = ['Name', 'Price', 'Rating']

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(products_data)

print(f"Successfully scraped {len(products_data)} books and saved to {csv_file}")
