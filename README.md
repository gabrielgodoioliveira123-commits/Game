# Game

Implementação mínima de um protocolo de resposta estruturada para um agente virtual
orientado por simbose semântica.

## Como validar

```bash
python -m unittest discover -s tests
```

## Uso rápido

```python
from semantic_symbiosis import criar_resposta_estruturada

resposta = criar_resposta_estruturada(
    analise_requisitos="Resumo do pedido.",
    estrategia_logica="Estratégia modular.",
    implementacao_tecnica="```python\nprint('ok')\n```",
    guia_integracao="Encadear o Markdown com o agente principal.",
    validacao_sanidade="Saída coerente e segura.",
)

print(resposta.para_markdown())
```
