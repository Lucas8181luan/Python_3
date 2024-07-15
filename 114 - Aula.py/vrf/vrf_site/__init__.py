def verificar_site(url):
    import requests
    try:
        resposta = requests.get(url, allow_redirects=True)
        if resposta.status_code == 200 or resposta.status_code == 301 or resposta.status_code == 302:
           print("Consegui acessar o site com sucesso!")
    except requests.ConnectionError:
        print("O site não está acessível no momento.")
