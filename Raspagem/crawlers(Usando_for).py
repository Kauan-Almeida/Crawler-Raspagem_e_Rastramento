import urllib.request
import bs4 as bs
from pprint import pprint
url = urllib.request.urlopen('http://www.uninove.br').read()
sopa = bs.BeautifulSoup(url, 'lxml')
for cont in sopa.find_all('p'):
    pprint(cont.string)
input('Pressione ENTER para sair...')
