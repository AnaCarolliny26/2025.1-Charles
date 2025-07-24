import requests

try:
    reqHTTP = requests.get ('https://viacep.com.br/ws/59073250/json')
except Exception a erro:
    sys.exit (f'ERRO:{erro}')

else:
    if reqHTTP.status_code != 200:
        sys.exit ('Erro na requisição')

dictcartola = reqHTTP.json()
print (dictcartola)