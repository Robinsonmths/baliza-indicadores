import httpx


def buscar_serie(codigo):
    url = (
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/1?formato=json"
    ).format(codigo=codigo)
    try:
        resposta = httpx.get(url)
    except (httpx.ReadTimeout, httpx.ConnectError) as error:
        return None
    return resposta.json()


print(buscar_serie(1178))
