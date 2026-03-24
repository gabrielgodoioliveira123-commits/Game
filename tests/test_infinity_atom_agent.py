import json
import tempfile
import unittest

from infinity_atom_agent import InfinityAtomAgent, RankingUpdater, ReadingModule


class InfinityAtomAgentTests(unittest.TestCase):
    def test_analyze_situation_updates_emotion_memory_and_verdict(self) -> None:
        agent = InfinityAtomAgent()

        result = agent.analyze_situation(
            {
                "evento": "batalha iminente",
                "proposição": "Mentir é errado em qualquer contexto.",
            }
        )

        self.assertEqual(result["dominant_emotion"], "antecipação")
        self.assertEqual(result["moral_verdict"], "errado")
        self.assertEqual(result["memory_count"], 1)
        self.assertIn("hipótese", result["selected_scenario"])
        self.assertEqual(
            set(result["philosophy_scores"]),
            set(agent.philosophy_engine.schools),
        )

    def test_reading_helpers_ignore_blank_lines_safely(self) -> None:
        text = "Primeiro parágrafo.\n\n   \nSegundo bloco com ciência."

        self.assertEqual(ReadingModule.skimming(text), ["Primeiro", "Segundo"])
        self.assertEqual(
            InfinityAtomAgent().read_text(text)["read"],
            ["Primeiro parágrafo.", "Segundo bloco com ciência."],
        )

    def test_update_rankings_loads_json_and_missing_file_returns_empty(self) -> None:
        with tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete=False) as handle:
            json.dump({"matemática": "Ada Lovelace"}, handle)
            handle.flush()
            updater = RankingUpdater(handle.name)
            self.assertEqual(updater.update(), {"matemática": "Ada Lovelace"})

        self.assertEqual(RankingUpdater("/tmp/arquivo-inexistente.json").update(), {})

    def test_memory_recall_and_simulated_learning(self) -> None:
        agent = InfinityAtomAgent()

        agent.simulate_learning("lógica")
        recalled = agent.recall_memory()

        self.assertEqual(recalled, "Aprendizado sobre lógica")
        self.assertGreater(agent.emotion_engine.emotions["alegria"], 0.0)


if __name__ == "__main__":
    unittest.main()
