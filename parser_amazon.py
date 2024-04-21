import requests
from bs4 import BeautifulSoup
import csv
import time


def parser_amazon(search, pages):
    base_url = f"https://www.amazon.com/s?k={search}"


    with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price', 'Rating'])

        for page_num in range(1, pages+1):
            url = f"{base_url}&page={page_num}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('div', {'data-component-type': 's-search-result'})

            for product in products:
                
                try:
                    product_name = product.find('span', {'class': 'a-text-normal'}).text.strip()
                except AttributeError:
                    product_name = "N/A"

                try:
                    price = product.find('span', {'class': 'a-offscreen'}).text.strip()
                except AttributeError:
                    price = "N/A"

                try:
                    rating = product.find('span', {'class': 'a-icon-alt'}).text.strip()
                except AttributeError:
                    rating = "N/A"

                writer.writerow([product_name, price, rating])

            time.sleep(20)
