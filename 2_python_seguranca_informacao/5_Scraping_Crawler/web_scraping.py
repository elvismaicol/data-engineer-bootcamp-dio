from bs4 import BeautifulSoup
import requests

# obj site esta recebendo o conteudo da requisição http do site
site = requests.get("https://www.climatempo.com.br/").content

# obj soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

# transforma html em string, e o print vai exibir o html na tela
# print(soup.prettify())

# img alt="Temperatura mínima Quarta" class="_margin-r-5" height="12" src="/dist/images/v2/svg/ic-arrow-min.svg" width="12"/>
temperartura = soup.find("h3", class_="title -gray-dark-2 _margin-b-10")

print(temperartura.string)

print(soup.title)
print(soup.title.string)

print(soup.a)

print(soup.p)
print(soup.p.string)

# busca informações relacionadas ao adm da pagina
print(soup.find('admin'))
