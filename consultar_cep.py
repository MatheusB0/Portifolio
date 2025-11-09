import requests

def consulta_cep(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"
  res = requests.get(url)
  res = res.json()
  return (res['logradouro'], res["bairro"],res["localidade"], res['uf'])