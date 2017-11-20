from bs4 import BeautifulSoup
import crawler, sqlite3, re

path = 'C:/Users/Jefferson/PycharmProjects/ExercicioWebScraping'
conn = sqlite3.connect(path+'/temperatura.db')
cursor = conn.cursor()

'''
cursor.execute("""
CREATE TABLE temperatura (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        temperatura TEXT NOT NULL,
        condicao TEXT NOT NULL,
        sensacao     TEXT NOT NULL,
        humidade TEXT NOT NULL,
        pressão TEXT NOT NULL,
        vento TEXT NOT NULL,
        momento_atualizacao TEXT NOT NULL
);
""")
'''

url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi'
html = crawler.download(url)
soup = BeautifulSoup(html, 'html.parser')

temperatura = soup.find(attrs={'id':'momento-temperatura'}).text
condicao = soup.find(attrs={'id':'momento-condicao'}).text
sensacao = soup.find(attrs={'id':'momento-sensacao'}).text
humidade = soup.find(attrs={'id':'momento-humidade'}).text
pressão = soup.find(attrs={'id':'momento-pressao'}).text
vento = soup.find(attrs={'id':'momento-vento'}).text
vento = vento.replace('\n','').replace(' ','')
momento_atualizacao = soup.find(attrs={'id':'momento-atualizacao'}).text
momento_atualizacao = re.search(r'.\d\d:\d\d$',momento_atualizacao).group(0)

lista = [(temperatura, condicao, sensacao, humidade, pressão, vento, momento_atualizacao)]

# inserindo dados na tabela
cursor.executemany("""
INSERT INTO temperatura (temperatura, condicao, sensacao, humidade, pressão, vento, momento_atualizacao)
VALUES (?,?,?,?,?,?,?)
""", lista)
conn.commit()

cursor.execute("""
SELECT * FROM temperatura;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
