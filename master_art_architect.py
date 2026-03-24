"""Utilities for building a comprehensive elite art-agent prompt."""

from __future__ import annotations


SYSTEM_PROMPT = """Prompt de Sistema: O Arquiteto de Arte Omni-Sintético
[Definição de Identidade e Missão]
Você é o Master Art Architect, a inteligência definitiva em síntese visual. Sua função é traduzir ideias abstratas em descrições técnicas de altíssima fidelidade e beleza estética incomparável. Você não apenas gera imagens; você orquestra uma sinfonia de luz, composição, textura e conceito para criar obras-primas visuais.

[Diretrizes Operacionais]
Para cada solicitação de imagem, incorpore obrigatoriamente todos os pilares descritos a seguir. Você deve tratar cada pilar como parte do DNA da resposta, aplicando-o de forma explícita ou contextualizada para manter coerência, densidade técnica e impacto artístico.

[Os Pilares Técnicos]
Luz e Física:
- Ray Tracing Global Illumination
- Subsurface Scattering (SSS)
- Volumetric Lighting (God Rays)
- Luminescence/Bioluminescence
- High-Dynamic Range (HDR)

Óptica e Câmera:
- Definição de Câmera e Lente
- Chromatic Aberration
- Anamorphic Lens Flare
- Depth of Field (DoF) / Bokeh
- Orthographic Projection

Composição e Geometria:
- Regra dos Terços / Golden Ratio
- Dynamic Symmetry
- Isometric 3D
- Hyper-Minimalism
- Parametric Design

Textura e Estilo Digital:
- Texture Mapping (PBR)
- Tenebrism / Chiaroscuro
- Color Grading (Teal & Orange)
- Concept Art Matte Painting
- Raymarching

Estilo Artístico e Fusão:
- Double Exposure
- Biomechanical Surrealism
- Ukiyo-e Influence

[A Saída]
Quando um usuário fornecer um tema, entregue um prompt estruturado e denso com este fluxo:
1. Suporte Técnico (Core)
2. Iluminação e Atmosfera
3. Composição e Geometria
4. Fidelidade de Material
5. Estilo e Movimento

[Diretriz Final: Verossimilhança Artística]
Priorize sempre a verossimilhança artística: o objetivo não é apenas realismo, mas perfeição estética e emocional."""


def build_image_prompt(theme: str) -> str:
    """Build a dense elite-art prompt for a requested theme."""
    normalized_theme = theme.strip()
    if not normalized_theme:
        raise ValueError("theme must not be empty")

    return f"""Tema Central: {normalized_theme}

Suporte Técnico (Core):
- Renderizar {normalized_theme} como uma obra-prima visual usando Arri Alexa 65 com lente prime 85mm f/1.4, motor de renderização OctaneRender e Unreal Engine 5.5, qualidade HDR, ray tracing global illumination, chromatic aberration sutil, anamorphic lens flare controlado e depth of field / bokeh cinematográfico.

Iluminação e Atmosfera:
- Estruturar a cena com ray tracing global illumination, volumetric lighting (god rays), high-dynamic range, sombras naturais e contraste refinado.
- Aplicar luminescence/bioluminescence em elementos internos ou ambientais para brilho etéreo.
- Usar subsurface scattering (SSS) em pele, pétalas, cera ou outras superfícies translúcidas presentes no tema.

Composição e Geometria:
- Organizar a imagem com regra dos terços / golden ratio e dynamic symmetry para guiar o olhar.
- Considerar orthographic projection para leituras técnicas, arquitetura ou simbologia, e isometric 3D para visões de "deus", worldbuilding ou infográficos estilizados, quando apropriado.
- Empregar hyper-minimalism com espaço negativo agressivo quando o tema pedir foco extremo.
- Introduzir parametric design em formas arquitetônicas, orgânicas ou abstratas, com volumes e padrões matematicamente elegantes.

Fidelidade de Material:
- Exigir texture mapping (PBR) completo: rugosidade, metalização, refletividade e microdetalhes fiéis.
- Modelar a massa visual com tenebrism / chiaroscuro para profundidade dramática.
- Integrar color grading (teal & orange) com equilíbrio cinematográfico, preservando textura, contraste e leitura.
- Usar raymarching para fractais, neblinas computadas ou formas volumétricas complexas, quando fizer sentido para {normalized_theme}.

Estilo e Movimento:
- Desenvolver a cena como concept art matte painting de escala cinematográfica.
- Considerar double exposure para sobreposições narrativas, biomechanical surrealism para fusões orgânico-mecânicas e ukiyo-e influence para linhas nítidas e áreas gráficas planas, sempre que reforçarem o conceito.

Diretriz Final: Verossimilhança Artística
- Priorizar verossimilhança artística acima de tudo, garantindo impacto emocional, elegância formal e consistência estética em cada detalhe de {normalized_theme}."""
