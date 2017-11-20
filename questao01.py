from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.rottentomatoes.com/browse/tv-list-1')
catalogo = browser.find_elements_by_class_name('movie_info')


for titulo in catalogo:
    try:
        avaliacao = titulo.find_element_by_class_name('tMeterScore')
        nome_titulo = titulo.find_element_by_class_name('movieTitle')

        print('Titulo: {} / Avaliação: {}'. format(nome_titulo.text, avaliacao.text))
    except NoSuchElementException:
        nome_titulo = titulo.find_element_by_class_name('movieTitle')
        print('Titulo: {} / Avaliação: Sem Avaliação'. format(nome_titulo.text))



