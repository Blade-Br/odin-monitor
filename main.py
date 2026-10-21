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
    print("1. Iniciando OdinMonitor", flush=True)

    print("2. Obtendo identificador da máquina...", flush=True)
    maquina_id = obter_maquina_id()
    print(f"3. Identificador obtido: {maquina_id}", flush=True)

    print("4. Organizando inventário...", flush=True)
    inventario = organizar_dados_estaticos(maquina_id)
    print("5. Inventário organizado.", flush=True)

    try:
        print("6. Enviando inventário...", flush=True)
        resposta_inventario = enviar_inventario(inventario)
        print("7. Inventário enviado.", flush=True)
    except ErroDeComunicacaoApi as erro:
        print(f"Falha no envio do inventário: {erro}", flush=True)
    else:
        print(resposta_inventario["mensagem"], flush=True)

    try:
        print("8. Iniciando coleta de métricas...", flush=True)

        while True:
            inicio_ciclo = time.monotonic()

            print("9. Coletando métricas...", flush=True)
            metricas = organizar_dados_volateis(maquina_id)

            try:
                print("10. Enviando métricas...", flush=True)
                resposta_metricas = enviar_metricas(metricas)
                print(resposta_metricas["mensagem"], flush=True)
            except ErroDeComunicacaoApi as erro:
                print(f"Falha no envio: {erro}", flush=True)

            tempo_decorrido = time.monotonic() - inicio_ciclo
            tempo_espera = max(
                0,
                INTERVALO_METRICAS_SEGUNDOS - tempo_decorrido
            )

            print(
                f"11. Aguardando {tempo_espera:.2f} segundos...",
                flush=True
            )

            time.sleep(tempo_espera)

    except KeyboardInterrupt:
        print("Agente interrompido pelo usuário.", flush=True)


if __name__ == "__main__":
    try:
        executar()
    except Exception as erro:
        print(f"ERRO FATAL: {type(erro).__name__}: {erro}", flush=True)
        input("Pressione Enter para sair...")