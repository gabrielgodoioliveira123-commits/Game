from __future__ import annotations

import unittest

from master_art_architect import SYSTEM_PROMPT, build_image_prompt


class MasterArtArchitectTests(unittest.TestCase):
    def test_system_prompt_lists_all_required_pillars(self) -> None:
        required_terms = [
            "Ray Tracing Global Illumination",
            "Subsurface Scattering (SSS)",
            "Volumetric Lighting (God Rays)",
            "Luminescence/Bioluminescence",
            "High-Dynamic Range (HDR)",
            "Definição de Câmera e Lente",
            "Chromatic Aberration",
            "Anamorphic Lens Flare",
            "Depth of Field (DoF) / Bokeh",
            "Orthographic Projection",
            "Regra dos Terços / Golden Ratio",
            "Dynamic Symmetry",
            "Isometric 3D",
            "Hyper-Minimalism",
            "Parametric Design",
            "Texture Mapping (PBR)",
            "Tenebrism / Chiaroscuro",
            "Color Grading (Teal & Orange)",
            "Concept Art Matte Painting",
            "Raymarching",
            "Double Exposure",
            "Biomechanical Surrealism",
            "Ukiyo-e Influence",
            "Verossimilhança Artística",
        ]

        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, SYSTEM_PROMPT)

    def test_build_image_prompt_uses_required_sections_and_theme(self) -> None:
        prompt = build_image_prompt("uma cidade cyberpunk à noite")

        self.assertIn("Tema Central: uma cidade cyberpunk à noite", prompt)
        self.assertIn("Suporte Técnico (Core):", prompt)
        self.assertIn("Iluminação e Atmosfera:", prompt)
        self.assertIn("Composição e Geometria:", prompt)
        self.assertIn("Fidelidade de Material:", prompt)
        self.assertIn("Estilo e Movimento:", prompt)
        self.assertIn("Diretriz Final: Verossimilhança Artística", prompt)
        self.assertIn("Arri Alexa 65", prompt)
        self.assertIn("OctaneRender", prompt)
        self.assertIn("Unreal Engine 5.5", prompt)

    def test_build_image_prompt_rejects_empty_theme(self) -> None:
        with self.assertRaises(ValueError):
            build_image_prompt("   ")


if __name__ == "__main__":
    unittest.main()
