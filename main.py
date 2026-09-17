import time

from config import INTERVALO_METRICAS_SEGUNDOS
from Modelos.metricas import organizar_dados_estaticos
from Modelos.metricas import organizar_dados_volateis
from Servicos.api import (
    ErroDeComunicacaoApi,
    enviar_inventario,
    enviar_metricas,
)
from Servicos.identidade import obter_maquina_id


def executar():
    maquina_id = obter_maquina_id()
    inventario = organizar_dados_estaticos(maquina_id)

    try:
        resposta_inventario = enviar_inventario(inventario)
    except ErroDeComunicacaoApi as erro:
        print(f"Falha no envio: {erro}")
    else:
        print(resposta_inventario["mensagem"])

    try:
        while True:
            inicio_ciclo = time.monotonic()
            metricas = organizar_dados_volateis(maquina_id)

            try:
                resposta_metricas = enviar_metricas(metricas)
                print(resposta_metricas["mensagem"])
            except ErroDeComunicacaoApi as erro:
                print(f"Falha no envio: {erro}")

            tempo_decorrido = time.monotonic() - inicio_ciclo
            tempo_espera = max(
                0,
                INTERVALO_METRICAS_SEGUNDOS - tempo_decorrido
            )
            time.sleep(tempo_espera)
    except KeyboardInterrupt:
        print("Agente interrompido pelo usuário.")


if __name__ == "__main__":
    executar()
