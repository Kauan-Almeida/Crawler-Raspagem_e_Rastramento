import urllib.request
import bs4 as bs
url = urllib.request.urlopen('http://uninove.br').read()
sopa = bs.BeautifulSoup(url, 'lxml')
print(sopa.h1.text)
input('Pressione Enter para sair...')
