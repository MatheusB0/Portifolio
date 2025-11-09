import requests
def cotar(data):
        url = (
            "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            "CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao="
            f"'{data}'&$format=json"
        )
        res = requests.get(url)
        res.raise_for_status() 
        dados = res.json()

        if dados.get("value"):
            return dados["value"][0]["cotacaoVenda"]
        return None
    