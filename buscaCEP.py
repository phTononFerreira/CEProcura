from distutils.filelist import findall
import requests
from bs4 import BeautifulSoup

def buscarCEP(CEP, show=False):
    try:
        CEP = CEP.replace('-', '')
        if len(CEP)>8: raise ValueError()
        if show: print("BUSCANDO...")
        url = f"https://cep.guiamais.com.br/busca?word={CEP}"
        content = requests.get(url).content
        site = BeautifulSoup(content, 'html.parser')
        allTables = site.findAll('tr')
        allTables.pop(0)
        resultados = []
        for table in allTables:
            rua = table.findAll('td')[0].text
            cep = table.findAll('td')[-1].text
            rua = rua.replace('\n', '')
            bairro,cidade,estado = table.find('td', attrs={'class': 'hidden-lg'}).text.split(', ')
            resultados.append({'cep': cep, 'estado': estado, 'bairro': bairro, 'cidade': cidade, 'rua':rua})
        return resultados
    except ValueError:
        return False
    except: 
        return False

if __name__ == '__main__':
    resultados = buscarCEP(input("DIGITE O CEP: "),show=True)
    if resultados:
        print("RESULTADOS:")
        for t in resultados:
            print()
            print(f"CEP: {t['cep']}")
            print(f"ESTADO: {t['estado']}")
            print(f"CIDADE: {t['cidade']}")
            print(f"BAIRRO: {t['bairro']}")
            print(f"RUA: {t['rua']}")
    input('>> PRESSIONE ENTER PARA SAIR...')
