from Coletores.cpu import (
    coletar_cpu_estatica,
    coletar_cpu_volatil
)

from Coletores.memoria import (
    coletar_memoria_fisica_estatica,
    coletar_memoria_fisica_volatil,
    coletar_memoria_virtual_estatica,
    coletar_memoria_virtual_volatil
)

from Coletores.disco import (
    coletar_disco_estatico,
    coletar_disco_volatil
)

from Coletores.rede import (
    coletar_rede_volatil
)

from Coletores.sistema import (
    coletar_sistema_estatico,
    coletar_uptime,
    coletar_timestamp,
    # coletar_top_processos
)


# ==========================================
# DADOS ESTÁTICOS
# ==========================================

def organizar_dados_estaticos(maquina_id: str):

    sistema = coletar_sistema_estatico()

    return {

        "maquina_id": maquina_id,

        "identificacao": {
            "hostname": sistema["hostname"],
            "sistema_operacional": sistema[
                "sistema_operacional"
            ],
            "versao": sistema["versao"]
        },

        "cpu": coletar_cpu_estatica(),

        "memoria": {

            "memoria_fisica":
                coletar_memoria_fisica_estatica(),

            "memoria_virtual":
                coletar_memoria_virtual_estatica()
        },

        "discos": coletar_disco_estatico()
    }


# ==========================================
# DADOS VOLÁTEIS
# ==========================================

def organizar_dados_volateis(maquina_id: str):

    return {

        "maquina_id": maquina_id,

        "timestamp": coletar_timestamp(),

        "cpu": coletar_cpu_volatil(),

        "memoria": {

            "memoria_fisica":
                coletar_memoria_fisica_volatil(),

            "memoria_virtual":
                coletar_memoria_virtual_volatil()
        },

        "discos": coletar_disco_volatil(),

        "rede": coletar_rede_volatil(),

        "sistema": {

            "uptime_segundos":
                coletar_uptime(),

            #"top_processos":
            #    coletar_top_processos()
        }
    }
