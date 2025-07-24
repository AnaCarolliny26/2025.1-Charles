import requestS, sys

strCEP = input ('Informe o CEP:')

try:
    reqHTTP = requests.get ('https://api.cartolafc.globo.com/atletas/mercado')
except Exception a erro:
    sys.exit (f'ERRO:{erro}')

else:
    if reqHTTP.status_code != 200:
        sys.exit ('Erro na requisição')

dictcartola = reqHTTP.json()
print (dictcartola)