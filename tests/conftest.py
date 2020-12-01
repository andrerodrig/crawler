import pytest
import crawler.correios as c
from selenium import webdriver


@pytest.fixture(scope='module')
def create_htmlobj():

    array_ufs = [
        "AC",
        "AL",
        "AM",
        "AP",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MG",
        "MS",
        "MT",
        "PA",
        "PB",
        "PE",
        "PI",
        "PR",
        "RJ",
        "RN",
        "RO",
        "RR",
        "RS",
        "SC",
        "SE",
        "SP",
        "TO",
    ]

    ff = webdriver.Firefox()
    htmlobj = c.HtmlObject(ff, "https://www.google.com")
    htmlobj._HtmlObject__ufs = array_ufs
    return htmlobj
