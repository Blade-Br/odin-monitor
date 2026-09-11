import psutil
import socket
import time
import subprocess


# ==============================
# CONEXÃO COM A INTERNET
# ==============================

def verificar_conexao():

    try:
        socket.create_connection(
            ("8.8.8.8", 53),
            timeout=3
        )

        return True

    except OSError:
        return False


# ==============================
# NOME DA REDE
# ==============================

def coletar_nome_rede_wifi():

    try:

        resultado = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        for linha in resultado.stdout.splitlines():

            linha = linha.strip()

            if linha.startswith("SSID") and "BSSID" not in linha:

                return linha.split(":", 1)[1].strip()

    except Exception:

        return None

    return None

# ==============================
# ENDEREÇO IPV4
# ==============================

def coletar_ipv4():

    interfaces = psutil.net_if_addrs()
    status_interfaces = psutil.net_if_stats()

    for nome, enderecos in interfaces.items():

        if not status_interfaces[nome].isup:
            continue

        for endereco in enderecos:

            if endereco.family == socket.AF_INET:

                if endereco.address != "127.0.0.1":
                    return endereco.address

    return None


# ==============================
# TAXA DE DOWNLOAD E UPLOAD
# ==============================

def coletar_taxa_rede():

    dados_iniciais = psutil.net_io_counters()

    time.sleep(1)

    dados_finais = psutil.net_io_counters()

    download_mb_s = (
        dados_finais.bytes_recv -
        dados_iniciais.bytes_recv
    ) / (1024 ** 2)

    upload_mb_s = (
        dados_finais.bytes_sent -
        dados_iniciais.bytes_sent
    ) / (1024 ** 2)

    return {
        "download_mb_s": round(download_mb_s, 2),
        "upload_mb_s": round(upload_mb_s, 2)
    }


# ==============================
# INFORMAÇÕES VOLÁTEIS
# ==============================

def coletar_rede_volatil():

    conectado = verificar_conexao()

    # Caso não exista conexão com a internet
    if not conectado:

        return {
            "conectado": False,
            "nome_rede": None,
            "ipv4": None,
            "download_mb_s": 0,
            "upload_mb_s": 0
        }

    taxas = coletar_taxa_rede()

    return {
        "conectado": True,

        "nome_rede": coletar_nome_rede_wifi(),

        "ipv4": coletar_ipv4(),

        "download_mb_s": taxas["download_mb_s"],

        "upload_mb_s": taxas["upload_mb_s"]
    }


# ==============================
# FUNÇÃO PRINCIPAL
# ==============================

def coletar_rede():

    return {
        "volateis": coletar_rede_volatil()
    }