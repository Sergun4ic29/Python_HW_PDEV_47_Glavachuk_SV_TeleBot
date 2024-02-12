import requests
from bs4 import BeautifulSoup


TOKEN = '6757006081:AAHC20PF2wBxG5q4OmuV5BeTDWQETyJTWWE'
#CRYPTO = '858e0840e3170d1f307c3d1f7dd36750d812ed1ba742e31814560897c778ff6c'
keys = {}
if __name__ != "__main__":
    page = requests.get('https://coinmarketcap.com/ru/all/views/all/').text
    soup = BeautifulSoup(page,'lxml')
    block = soup.find_all('a',class_='cmc-table__column-name--symbol cmc-link')
    for m_str in block:
        keys[m_str['title']] = m_str.text



