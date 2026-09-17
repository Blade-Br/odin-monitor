import psutil
import platform
import socket
from datetime import datetime, timezone


# ==============================
# INFORMAÇÕES ESTÁTICAS
# ==============================

def coletar_sistema_estatico():

    return {
        "hostname": socket.gethostname(),

        "sistema_operacional": platform.system(),

        "versao": platform.release()
    }


# ==============================
# UPTIME
# ==============================

def coletar_uptime():

    tempo_inicial = psutil.boot_time()

    uptime_segundos = datetime.now().timestamp() - tempo_inicial

    return round(uptime_segundos)


# ==============================
# TIMESTAMP
# ==============================

def coletar_timestamp():

    # O contrato do Odin Server exige uma data/hora com fuso horário.
    # UTC evita ambiguidade entre máquinas monitoradas em fusos diferentes.
    return datetime.now(timezone.utc).isoformat()


# ==============================
# TOP PROCESSOS
# ==============================

def coletar_top_processos(limite=5):

    processos = []

    for processo in psutil.process_iter(
        ["pid", "name", "cpu_percent"]
    ):

        try:

            processos.append({
                "nome": processo.info["name"],
                "pid": processo.info["pid"],
                "uso_cpu_percentual": processo.info["cpu_percent"]
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            continue

    processos_ordenados = sorted(
        processos,
        key=lambda processo: processo[
            "uso_cpu_percentual"
        ],
        reverse=True
    )

    return processos_ordenados[:limite]


# ==============================
# INFORMAÇÕES VOLÁTEIS
# ==============================

def coletar_sistema_volatil():

    return {
        "uptime_segundos": coletar_uptime(),

        "timestamp": coletar_timestamp(),

        "top_processos": coletar_top_processos()
    }


# ==============================
# FUNÇÃO PRINCIPAL
# ==============================

def coletar_sistema():

    return {
        "estaticos": coletar_sistema_estatico(),

        "volateis": coletar_sistema_volatil()
    }

# print(coletar_sistema())
