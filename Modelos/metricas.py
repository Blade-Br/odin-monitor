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

    print("4.1 Iniciando coleta do sistema...", flush=True)
    sistema = coletar_sistema_estatico()
    print("4.2 Coleta do sistema concluída.", flush=True)

    print("4.3 Coletando CPU...", flush=True)
    cpu = coletar_cpu_estatica()
    print("4.4 CPU concluída.", flush=True)

    print("4.5 Coletando memória física...", flush=True)
    memoria_fisica = coletar_memoria_fisica_estatica()
    print("4.6 Memória física concluída.", flush=True)

    print("4.7 Coletando memória virtual...", flush=True)
    memoria_virtual = coletar_memoria_virtual_estatica()
    print("4.8 Memória virtual concluída.", flush=True)

    print("4.9 Coletando discos...", flush=True)
    discos = coletar_disco_estatico()
    print("4.10 Discos concluídos.", flush=True)

    return {
        "maquina_id": maquina_id,

        "identificacao": {
            "hostname": sistema["hostname"],
            "sistema_operacional": sistema["sistema_operacional"],
            "versao": sistema["versao"]
        },

        "cpu": cpu,

        "memoria": {
            "memoria_fisica": memoria_fisica,
            "memoria_virtual": memoria_virtual
        },

        "discos": discos
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
