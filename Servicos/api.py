import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from config import API_BASE_URL, API_TIMEOUT_SEGUNDOS


class ErroDeComunicacaoApi(RuntimeError):
    """Erro que impede o Monitor de entregar dados ao Odin Server."""


def enviar_para_api(caminho: str, dados: dict) -> dict:
    """Envia um payload JSON ao Odin Server e devolve a resposta validada."""
    requisicao = Request(
        url=f"{API_BASE_URL}{caminho}",
        data=json.dumps(dados).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(requisicao, timeout=API_TIMEOUT_SEGUNDOS) as resposta:
            return json.loads(resposta.read().decode("utf-8"))
    except HTTPError as erro:
        detalhe = erro.read().decode("utf-8", errors="replace")
        raise ErroDeComunicacaoApi(
            f"Odin Server respondeu HTTP {erro.code}: {detalhe}"
        ) from erro
    except (URLError, TimeoutError) as erro:
        raise ErroDeComunicacaoApi(
            f"Não foi possível conectar ao Odin Server em {API_BASE_URL}."
        ) from erro


def enviar_inventario(dados: dict) -> dict:
    return enviar_para_api("/inventarios", dados)


def enviar_metricas(dados: dict) -> dict:
    return enviar_para_api("/metricas", dados)
