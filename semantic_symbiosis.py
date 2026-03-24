"""Ferramentas para estruturar respostas de um agente com simbiose semântica."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict


class SecaoResposta(Enum):
    """Representa a ordem canônica das seções da resposta do agente."""

    ANALISE_REQUISITOS = "Análise de Requisitos"
    ESTRATEGIA_LOGICA = "Estratégia Lógica (Chain of Thought)"
    IMPLEMENTACAO_TECNICA = "Implementação Técnica"
    GUIA_INTEGRACAO = "Guia de Integração"
    VALIDACAO_SANIDADE = "Validação de Sanidade"


class EstadoSistema(Enum):
    """Representa estados válidos do protocolo do agente virtual."""

    AGUARDANDO_COMANDO_INICIAL = "Aguardando comando inicial"


def _validar_secao(nome_secao: str, conteudo: str) -> str:
    """Valida o conteúdo textual de uma seção obrigatória.

    Args:
        nome_secao: Nome humano da seção que será validada.
        conteudo: Conteúdo textual informado para a seção.

    Returns:
        O conteúdo normalizado sem espaços excedentes nas bordas.

    Raises:
        TypeError: Quando o conteúdo não é uma string.
        ValueError: Quando a seção é vazia após a normalização.
    """

    if not isinstance(conteudo, str):
        raise TypeError(
            f"A seção '{nome_secao}' precisa ser uma string para manter a saída previsível."
        )

    conteudo_normalizado: str = conteudo.strip()
    if not conteudo_normalizado:
        raise ValueError(
            f"A seção '{nome_secao}' não pode ser vazia, pois o protocolo exige contexto completo."
        )

    return conteudo_normalizado


@dataclass(frozen=True)
class RespostaEstruturada:
    """Modela uma resposta imutável compatível com o protocolo do agente.

    Args:
        analise_requisitos: Resumo breve do entendimento dos requisitos.
        estrategia_logica: Explicação da arquitetura ou da linha de raciocínio adotada.
        implementacao_tecnica: Conteúdo técnico, podendo incluir bloco de código.
        guia_integracao: Explicação de como conectar a solução ao restante do sistema.
        validacao_sanidade: Confirmação final sobre segurança, eficiência e consistência.
        estado_sistema: Estado operacional atual do agente.
    """

    analise_requisitos: str
    estrategia_logica: str
    implementacao_tecnica: str
    guia_integracao: str
    validacao_sanidade: str
    estado_sistema: EstadoSistema = EstadoSistema.AGUARDANDO_COMANDO_INICIAL

    def __post_init__(self) -> None:
        """Garante que todas as seções obrigatórias estejam válidas desde a criação."""

        object.__setattr__(
            self,
            "analise_requisitos",
            _validar_secao(
                SecaoResposta.ANALISE_REQUISITOS.value, self.analise_requisitos
            ),
        )
        object.__setattr__(
            self,
            "estrategia_logica",
            _validar_secao(
                SecaoResposta.ESTRATEGIA_LOGICA.value, self.estrategia_logica
            ),
        )
        object.__setattr__(
            self,
            "implementacao_tecnica",
            _validar_secao(
                SecaoResposta.IMPLEMENTACAO_TECNICA.value,
                self.implementacao_tecnica,
            ),
        )
        object.__setattr__(
            self,
            "guia_integracao",
            _validar_secao(
                SecaoResposta.GUIA_INTEGRACAO.value, self.guia_integracao
            ),
        )
        object.__setattr__(
            self,
            "validacao_sanidade",
            _validar_secao(
                SecaoResposta.VALIDACAO_SANIDADE.value, self.validacao_sanidade
            ),
        )

    def para_dict(self) -> Dict[str, str]:
        """Converte a resposta para um dicionário simples e integrável.

        Returns:
            Um dicionário com o estado atual do sistema e todas as seções obrigatórias.
        """

        return {
            "estado_sistema": self.estado_sistema.value,
            "analise_requisitos": self.analise_requisitos,
            "estrategia_logica": self.estrategia_logica,
            "implementacao_tecnica": self.implementacao_tecnica,
            "guia_integracao": self.guia_integracao,
            "validacao_sanidade": self.validacao_sanidade,
        }

    def para_markdown(self) -> str:
        """Renderiza a resposta usando os delimitadores Markdown exigidos pelo protocolo.

        Returns:
            Uma string em Markdown com a ordem oficial das seções da resposta.
        """

        secoes_ordenadas = (
            (SecaoResposta.ANALISE_REQUISITOS, self.analise_requisitos),
            (SecaoResposta.ESTRATEGIA_LOGICA, self.estrategia_logica),
            (SecaoResposta.IMPLEMENTACAO_TECNICA, self.implementacao_tecnica),
            (SecaoResposta.GUIA_INTEGRACAO, self.guia_integracao),
            (SecaoResposta.VALIDACAO_SANIDADE, self.validacao_sanidade),
        )

        blocos_markdown = [
            f"## {secao.value}\n{conteudo}" for secao, conteudo in secoes_ordenadas
        ]
        blocos_markdown.append(
            f"**Estado do Sistema:** {self.estado_sistema.value}"
        )
        return "\n\n".join(blocos_markdown)


def criar_resposta_estruturada(
    analise_requisitos: str,
    estrategia_logica: str,
    implementacao_tecnica: str,
    guia_integracao: str,
    validacao_sanidade: str,
    estado_sistema: EstadoSistema = EstadoSistema.AGUARDANDO_COMANDO_INICIAL,
) -> RespostaEstruturada:
    """Cria uma resposta estruturada pronta para integração com o agente virtual.

    Args:
        analise_requisitos: Resumo breve do que foi compreendido.
        estrategia_logica: Explicação da estratégia escolhida para resolver a demanda.
        implementacao_tecnica: Bloco técnico da solução, incluindo código quando necessário.
        guia_integracao: Instruções de conexão com outros componentes do agente.
        validacao_sanidade: Confirmação final sobre segurança e eficiência.
        estado_sistema: Estado atual do ciclo de interação do agente.

    Returns:
        Uma instância imutável e validada de ``RespostaEstruturada``.
    """

    return RespostaEstruturada(
        analise_requisitos=analise_requisitos,
        estrategia_logica=estrategia_logica,
        implementacao_tecnica=implementacao_tecnica,
        guia_integracao=guia_integracao,
        validacao_sanidade=validacao_sanidade,
        estado_sistema=estado_sistema,
    )
