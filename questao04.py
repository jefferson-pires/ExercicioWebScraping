from bs4 import BeautifulSoup
import time, crawler

html = ' '
paises = []
count = 0

def tratar(valor):
    novo = valor.replace(',', '')
    for letra in novo:
        if letra >='a' and letra <= 'z':
            novo = novo.replace(letra, "")
    return novo

while html != 'Invalid record':
    url = 'http://example.webscraping.com/places/default/view/-'
    count += 1
    url = 'http://example.webscraping.com/places/default/view/-{}'.format(count)
    html = crawler.download(url)
    paises.append(html)
    time.sleep(10)

for link in paises:
    soup = BeautifulSoup(link, 'html.parser')

    #pegando valor da area
    tr = soup.find(attrs={'id': 'places_area__row'})
    td = tr.find(attrs={'class': 'w2p_fw'})
    area = float(tratar(td.text))

    #pegando valor da população
    tr = soup.find(attrs={'id': 'places_population__row'})
    td = tr.find(attrs={'class': 'w2p_fw'})
    população = float(tratar(td.text))

    #pegando nome do pais
    tr = soup.find(attrs={'id': 'places_country__row'})
    td = tr.find(attrs={'class': 'w2p_fw'})
    pais = td.text

    if area == 0 :
        densidade = 'não foi possivel calcular'
    else:
        densidade = população / area

    print('Pais: {} / Densidade Populacional: {}'. format(pais,densidade))


