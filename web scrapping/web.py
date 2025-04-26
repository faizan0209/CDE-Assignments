import requests
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/'

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('h3')
book_links = [base_url + book.find('a')['href'] for book in books]

for link in book_links:
    book_response = requests.get(link)
    book_soup = BeautifulSoup(book_response.text, 'html.parser')

    title = book_soup.find('div', class_='product_main').find('h1').text

    table = book_soup.find('table', class_='table table-striped')

    author = publisher = price = "Not Available"  

    if table:
        rows = table.find_all('tr')
        for row in rows:
            heading = row.find('th').text.strip()
            value = row.find('td').text.strip()

            if heading == 'UPC':  
                pass
            elif heading == 'Product Type':
                publisher = value  
            elif heading == 'Availability':
                author = value     
            elif heading == 'Price (excl. tax)':
                price = value       

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Publisher: {publisher}")
    print(f"Price: {price}")
    print('-' * 40)
