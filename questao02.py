from bs4 import BeautifulSoup
import csv, crawler

url = 'http://www.imdb.com/chart/boxoffice'
html = crawler.download(url)
soup = BeautifulSoup(html, 'html.parser')

tabela = soup.find(attrs={'class':'chart full-width'})
titulos = tabela.findAll(attrs={'class':'titleColumn'})
valores_acumulado = tabela.findAll(attrs={'class':'secondaryInfo'})
semanas = tabela.findAll(attrs={'class':'weeksColumn'})

try:
    f = open('tabela.csv', 'w')
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(('nome', 'valor','semanas'))

    for x in range(len(valores_acumulado)):
        titulo = titulos[x].text.strip()
        valor_acumulado = valores_acumulado[x].text.strip()
        semana = semanas[x].text.strip()
        writer.writerow((titulo, valor_acumulado,semana))
finally:
    f.close()


