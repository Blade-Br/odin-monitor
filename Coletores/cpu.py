import psutil

# ==============================
# INFORMAÇÕES ESTÁTICAS
# ==============================

def coletar_cpu_estatica():

    return {
        "nucleos_fisicos": psutil.cpu_count(logical=False),
        "nucleos_logicos": psutil.cpu_count(logical=True)
    }

# ==============================
# INFORMAÇÕES VOLÁTEIS
# ==============================

def coletar_cpu_volatil():

    uso_total = psutil.cpu_percent(interval=1)

    uso_por_nucleo = psutil.cpu_percent(
        interval=None,
        percpu=True
    )

    frequencia = psutil.cpu_freq()

    return {
        "uso_percentual": uso_total,

        "frequencia_ghz": (
            round(frequencia.current / 1000, 2)
            if frequencia else None
        ),

        "uso_por_nucleo": uso_por_nucleo
    }

# ===========================================

def coletar_cpu():

    return {
        "estaticos": coletar_cpu_estatica(),
        "volateis": coletar_cpu_volatil()
    }

# print(coletar_cpu())