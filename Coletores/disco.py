import json
import subprocess
import psutil


# ==============================
# INFORMAÇÕES ESTÁTICAS
# ==============================

def coletar_tipo_disco(mountpoint):
    comando = (
        f"Get-Partition -DriveLetter '{mountpoint[0]}' | "
        "Get-Disk | "
        "Get-PhysicalDisk | "
        "Select-Object -ExpandProperty MediaType"
    )

    try:
        resultado = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                comando
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=True,
            timeout=10
        )

        tipo = resultado.stdout.strip()

        return tipo if tipo else None

    except (
        subprocess.SubprocessError,
        OSError
    ):
        return None


def coletar_disco_estatico():
    discos = []

    for particao in psutil.disk_partitions():

        try:
            uso = psutil.disk_usage(particao.mountpoint)

            discos.append({
                "nome": particao.mountpoint,
                "tipo": coletar_tipo_disco(particao.mountpoint) or "N/A",
                "capacidade_total_gb": round(
                    uso.total / (1024 ** 3), 2
                )
            })

        except (PermissionError, OSError):
            continue

    return discos


# ==============================
# INFORMAÇÕES VOLÁTEIS
# ==============================

def coletar_disco_volatil():
    discos = []

    for particao in psutil.disk_partitions():

        try:
            uso = psutil.disk_usage(particao.mountpoint)

            discos.append({
                "nome": particao.mountpoint,

                "utilizado_gb": round(
                    uso.used / (1024 ** 3), 2
                ),

                "disponivel_gb": round(
                    uso.free / (1024 ** 3), 2
                )
            })

        except (PermissionError, OSError):
            continue

    return discos


# ==============================
# FUNÇÃO PRINCIPAL
# ==============================

def coletar_disco():
    return {
        "estaticos": coletar_disco_estatico(),
        "volateis": coletar_disco_volatil()
    }

#print(coletar_disco())
