import urllib.request
import bs4 as bs
from pprint import pprint
url = urllib.request.urlopen('http://www.uninove.br').read()
sopa = bs.BeautifulSoup(url, 'lxml')
pprint(sopa.find_all('i'))
input('Pressione ENTER para sair...')
