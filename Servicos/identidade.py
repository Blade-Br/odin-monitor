from uuid import UUID, uuid4

from config import ARQUIVO_IDENTIDADE


class IdentidadeInvalida(RuntimeError):
    """Indica que a identidade persistida do agente não é um UUID válido."""


def obter_maquina_id() -> str:
    """Obtém o UUID persistente da instalação ou cria-o na primeira execução."""
    if ARQUIVO_IDENTIDADE.exists():
        try:
            return str(UUID(ARQUIVO_IDENTIDADE.read_text(encoding="utf-8").strip()))
        except ValueError as erro:
            raise IdentidadeInvalida(
                f"A identidade em {ARQUIVO_IDENTIDADE} não é um UUID válido."
            ) from erro

    maquina_id = str(uuid4())
    ARQUIVO_IDENTIDADE.parent.mkdir(parents=True, exist_ok=True)

    arquivo_temporario = ARQUIVO_IDENTIDADE.with_suffix(".tmp")
    arquivo_temporario.write_text(maquina_id, encoding="utf-8")
    arquivo_temporario.replace(ARQUIVO_IDENTIDADE)

    return maquina_id
