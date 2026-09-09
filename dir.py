import requests
with open('wd.txt', 'r') as wd:
    diretorios = wd.read().splitlines()
    url = input("qual a url do site? exemplo https://nome.com.br/")
    for d in diretorios:
        respostas = requests.get(url + d)
        if respostas.status_code==200:
            print(f"diretorio encontrado {d} status {respostas.status_code}")
        else:
            print(f"não existe {d} status {respostas.status_code}")