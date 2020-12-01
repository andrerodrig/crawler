from selenium import webdriver
from crawler.correios import Correios


def crawler():
    """Collects data from the site passed"""
    ff = webdriver.Firefox()
    correios = Correios(
        ff,
        'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')
    correios.search_url()
    print("Buscando dados em todas as UFs")
    correios.search_all_ufs()
    print("Concluido!")
