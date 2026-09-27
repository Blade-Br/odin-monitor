import json

from Modelos.metricas import organizar_dados_estaticos
from Modelos.metricas import organizar_dados_volateis

from Servicos.identidade import obter_maquina_id


dados = {
    "estaticos": organizar_dados_estaticos(maquina_id=obter_maquina_id()),
    "volateis": organizar_dados_volateis(maquina_id=obter_maquina_id())
}

print(json.dumps(dados, indent=4, ensure_ascii=False))