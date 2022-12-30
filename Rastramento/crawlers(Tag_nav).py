#script com Error: 'NoneType' object has no attribute 'find_all'
import urllib.request
import bs4 as bs
from pprint import pprint
url = urllib.request.urlopen('http://www.uninove.br').read()
sopa = bs.BeautifulSoup(url, 'lxml')
navegacao = sopa.nav                 
for cont in navegacao.find_all('a'):
    print(cont.get('href'))
 
input('Pressione ENTER para sair...')
