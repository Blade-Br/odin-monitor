from Modelos.metricas import organizar_dados_estaticos
from Modelos.metricas import organizar_dados_volateis
import json

dadosE = organizar_dados_estaticos()
dadosV = organizar_dados_volateis()

print(json.dumps(
    dadosE,
    indent=4,
    ensure_ascii=False
))

print(json.dumps(
    dadosV,
    indent=4,
    ensure_ascii=False
)) 