"""Testes focados para o protocolo de resposta estruturada."""

from __future__ import annotations

import unittest

from semantic_symbiosis import EstadoSistema, criar_resposta_estruturada


class RespostaEstruturadaTestCase(unittest.TestCase):
    """Verifica o comportamento mínimo esperado pelo protocolo."""

    def test_deve_gerar_markdown_com_todas_as_secoes_em_ordem(self) -> None:
        """Garante que a saída preserve a estrutura exigida para integração previsível."""

        resposta = criar_resposta_estruturada(
            analise_requisitos="Resumo objetivo do pedido.",
            estrategia_logica="Plano modular e rastreável.",
            implementacao_tecnica="```python\nprint('ok')\n```",
            guia_integracao="Conectar ao orquestrador principal.",
            validacao_sanidade="Saída segura e consistente.",
        )

        markdown = resposta.para_markdown()

        self.assertIn("## Análise de Requisitos", markdown)
        self.assertIn("## Estratégia Lógica (Chain of Thought)", markdown)
        self.assertIn("## Implementação Técnica", markdown)
        self.assertIn("## Guia de Integração", markdown)
        self.assertIn("## Validação de Sanidade", markdown)
        self.assertTrue(
            markdown.endswith(
                "**Estado do Sistema:** Aguardando comando inicial"
            )
        )

    def test_deve_expor_saida_dict_para_integracao_programatica(self) -> None:
        """Garante um formato simples para consumo por outras aplicações ou agentes."""

        resposta = criar_resposta_estruturada(
            analise_requisitos="Entendimento validado.",
            estrategia_logica="Execução orientada por funções pequenas.",
            implementacao_tecnica="Código pronto para uso.",
            guia_integracao="Importar o módulo e renderizar em Markdown.",
            validacao_sanidade="Sem dependências externas.",
            estado_sistema=EstadoSistema.AGUARDANDO_COMANDO_INICIAL,
        )

        self.assertEqual(
            resposta.para_dict(),
            {
                "estado_sistema": "Aguardando comando inicial",
                "analise_requisitos": "Entendimento validado.",
                "estrategia_logica": "Execução orientada por funções pequenas.",
                "implementacao_tecnica": "Código pronto para uso.",
                "guia_integracao": "Importar o módulo e renderizar em Markdown.",
                "validacao_sanidade": "Sem dependências externas.",
            },
        )

    def test_deve_rejeitar_secao_vazia_com_mensagem_clara(self) -> None:
        """Evita respostas ambíguas que dificultam recuperação automática do agente."""

        with self.assertRaisesRegex(
            ValueError, "Análise de Requisitos.*não pode ser vazia"
        ):
            criar_resposta_estruturada(
                analise_requisitos="   ",
                estrategia_logica="Estratégia válida.",
                implementacao_tecnica="Implementação válida.",
                guia_integracao="Integração válida.",
                validacao_sanidade="Validação válida.",
            )


if __name__ == "__main__":
    unittest.main()
