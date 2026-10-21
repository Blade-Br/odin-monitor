import os
from pathlib import Path


API_BASE_URL = os.getenv("ODIN_SERVER_URL", "http://127.0.0.1:8000").rstrip("/")
API_TIMEOUT_SEGUNDOS = float(os.getenv("ODIN_API_TIMEOUT_SEGUNDOS", "10"))
API_LATENCIA_TIMEOUT_SEGUNDOS = float(
    os.getenv("ODIN_API_LATENCIA_TIMEOUT_SEGUNDOS", "1.5")
)
INTERVALO_METRICAS_SEGUNDOS = float(
    os.getenv("ODIN_INTERVALO_METRICAS_SEGUNDOS", "10")
)

if INTERVALO_METRICAS_SEGUNDOS <= 0:
    raise ValueError("ODIN_INTERVALO_METRICAS_SEGUNDOS deve ser maior que zero.")

PASTA_DADOS_AGENTE = Path(
    os.getenv(
        "ODIN_DADOS_DIR",
        str(Path(os.getenv("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "OdinMonitor"),
    )
)
ARQUIVO_IDENTIDADE = PASTA_DADOS_AGENTE / "identidade.txt"
