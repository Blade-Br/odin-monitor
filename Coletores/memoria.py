import psutil


# ==============================
# MEMÓRIA FÍSICA
# ==============================

def coletar_memoria_fisica_estatica():

    memoria = psutil.virtual_memory()

    return {
        "capacidade_total_gb": round(
            memoria.total / (1024 ** 3), 2
        )
    }


def coletar_memoria_fisica_volatil():

    memoria = psutil.virtual_memory()

    utilizado_gb = memoria.used / (1024 ** 3)
    disponivel_gb = memoria.available / (1024 ** 3)

    return {
        "memoria_utilizada_gb": round(utilizado_gb, 2),
        "memoria_utilizada_percentual": memoria.percent,

        "memoria_disponivel_gb": round(disponivel_gb, 2),
        "memoria_disponivel_percentual": round(
            (memoria.available / memoria.total) * 100, 2
        )
    }


# ==============================
# MEMÓRIA VIRTUAL (SWAP)
# ==============================

def coletar_memoria_virtual_estatica():

    memoria_virtual = psutil.swap_memory()

    return {
        "capacidade_total_gb": round(
            memoria_virtual.total / (1024 ** 3), 2
        )
    }


def coletar_memoria_virtual_volatil():

    memoria_virtual = psutil.swap_memory()

    utilizado_gb = memoria_virtual.used / (1024 ** 3)
    disponivel_gb = memoria_virtual.free / (1024 ** 3)

    percentual_disponivel = (
        (memoria_virtual.free / memoria_virtual.total) * 100
        if memoria_virtual.total > 0
        else 0
    )

    return {
        "memoria_utilizada_gb": round(utilizado_gb, 2),
        "memoria_utilizada_percentual": memoria_virtual.percent,

        "memoria_disponivel_gb": round(disponivel_gb, 2),
        "memoria_disponivel_percentual": round(
            percentual_disponivel, 2
        )
    }


# ==============================
# FUNÇÃO PRINCIPAL
# ==============================

def coletar_memoria():

    return {
        "memoria_fisica": {
            "estaticos": coletar_memoria_fisica_estatica(),
            "volateis": coletar_memoria_fisica_volatil()
        },

        "memoria_virtual": {
            "estaticos": coletar_memoria_virtual_estatica(),
            "volateis": coletar_memoria_virtual_volatil()
        }
    }

# print(coletar_memoria())