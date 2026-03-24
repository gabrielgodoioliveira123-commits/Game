from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


class EmotionEngine:
    """Simula emoções humanas utilizando categorias de Plutchik e estados complexos.

    Cada emoção é representada por um valor de intensidade entre 0 e 1.
    """

    def __init__(self) -> None:
        self.emotions: Dict[str, float] = {
            "alegria": 0.0,
            "tristeza": 0.0,
            "raiva": 0.0,
            "medo": 0.0,
            "nojo": 0.0,
            "desprezo": 0.0,
            "surpresa": 0.0,
            "confiança": 0.0,
            "repulsa": 0.0,
            "antecipação": 0.0,
            "amor": 0.0,
            "culpa": 0.0,
            "orgulho": 0.0,
            "melancolia": 0.0,
            "nostalgia": 0.0,
            "indignação": 0.0,
            "compaixão": 0.0,
            "vergonha": 0.0,
            "admiração": 0.0,
            "adoração": 0.0,
            "apreciação_estética": 0.0,
            "diversão": 0.0,
            "ansiedade": 0.0,
            "espanto": 0.0,
            "constrangimento": 0.0,
            "tédio": 0.0,
            "calma": 0.0,
            "confusão": 0.0,
            "desejo": 0.0,
            "dor_empática": 0.0,
            "encantamento": 0.0,
            "excitação": 0.0,
            "horror": 0.0,
            "interesse": 0.0,
            "alívio": 0.0,
            "romance": 0.0,
            "satisfação": 0.0,
            "desejo_sexual": 0.0,
            "respeito": 0.0,
            "esperança": 0.0,
            "frustração": 0.0,
            "entusiasmo": 0.0,
            "ciúme": 0.0,
            "gratidão": 0.0,
            "paz": 0.0,
        }

    def adjust(self, emotion: str, delta: float) -> None:
        """Ajusta a intensidade de uma emoção, limitando o valor entre 0 e 1."""
        if emotion not in self.emotions:
            raise KeyError(f"Emoção desconhecida: {emotion}")
        self.emotions[emotion] = max(0.0, min(1.0, self.emotions[emotion] + delta))

    def decay_all(self, factor: float = 0.9) -> None:
        """Aplica decaimento a todas as emoções para simular a passagem do tempo."""
        for key in self.emotions:
            self.emotions[key] *= factor

    def dominant(self) -> Optional[str]:
        """Retorna a emoção com maior intensidade no momento."""
        if not self.emotions:
            return None
        return max(self.emotions.items(), key=lambda item: item[1])[0]


class PhilosophyEngine:
    """Gerencia a influência de diversas correntes filosóficas."""

    def __init__(self) -> None:
        self.schools: Dict[str, Dict[str, Any]] = {
            "tomismo": {
                "princípios": [
                    "ordem e finalidade na natureza",
                    "existência de verdades objetivas",
                    "harmonia entre fé e razão",
                ],
            },
            "estoicismo": {
                "princípios": [
                    "virtude como bem supremo",
                    "controle das paixões",
                    "aceitação do destino",
                ],
            },
            "platonismo": {
                "princípios": [
                    "mundo das ideias como realidade última",
                    "importância da alma sobre o corpo",
                    "uso da dialética para alcançar a verdade",
                ],
            },
            "existencialismo": {
                "princípios": [
                    "liberdade individual e responsabilidade",
                    "absurdo da existência",
                    "criação de significado pessoal",
                ],
            },
            "empirismo": {
                "princípios": [
                    "conhecimento deriva da experiência sensorial",
                    "ceticismo quanto a ideias inatas",
                    "observação e experimentação como base científica",
                ],
            },
            "fenomenologia": {
                "princípios": [
                    "descrição rigorosa da experiência",
                    "suspensão de juízos pré-concebidos",
                    "intencionalidade da consciência",
                ],
            },
            "jungianismo": {
                "princípios": [
                    "inconsciente coletivo",
                    "arquétipos universais",
                    "processo de individuação",
                ],
            },
            "filosofias_orientais": {
                "princípios": [
                    "harmonia com o Tao",
                    "impermanência e desapego",
                    "não-dualidade",
                ],
            },
        }
        self.primary_school = "tomismo"

    def evaluate(self, situation: Dict[str, Any]) -> Dict[str, float]:
        """Retorna um escore de adequação para cada escola filosófica."""
        del situation
        return {name: random.random() for name in self.schools}


class EthicsEngine:
    """Aplica princípios morais objetivos baseados em doutrina tomista."""

    def __init__(self) -> None:
        self.objective_rules: List[str] = [
            "mentir é errado",
            "roubar é errado",
            "tratar os outros com dignidade e respeito",
        ]

    def judge(self, proposition: str) -> str:
        """Retorna um veredito moral: ``certo``, ``errado`` ou ``ambíguo``."""
        prop_lower = proposition.lower()
        for rule in self.objective_rules:
            if rule in prop_lower:
                return "errado"
        return "ambíguo"


class ScenarioEngine:
    """Gera e avalia múltiplos cenários mentais com base em trivium e quadrivium."""

    def __init__(self, max_scenarios: int = 100) -> None:
        self.max_scenarios = max_scenarios

    def generate_scenarios(self, situation: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Gera hipóteses distintas para uma situação."""
        scenarios = []
        for hypothesis in range(self.max_scenarios):
            variant = situation.copy()
            variant["hipótese"] = hypothesis
            scenarios.append(variant)
        return scenarios

    def evaluate_scenarios(self, scenarios: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Seleciona o cenário mais plausível."""
        return random.choice(scenarios) if scenarios else {}


class MemoryEngine:
    """Gerencia armazenamento e recuperação de memórias."""

    def __init__(self) -> None:
        self.memories: List[str] = []
        self.repetition_schedule: Dict[str, int] = {}

    def store(self, memory: str) -> None:
        self.memories.append(memory)
        self.repetition_schedule[memory] = 1

    def recall(self) -> Optional[str]:
        """Recupera a memória com menor número de revisões acumuladas."""
        if not self.memories:
            return None
        next_memory = min(self.repetition_schedule.items(), key=lambda item: item[1])[0]
        self.repetition_schedule[next_memory] += 1
        return next_memory


class ReadingModule:
    """Implementa técnicas de leitura e memorização para aquisição de conhecimento."""

    @staticmethod
    def sq3r(text: str) -> Dict[str, Any]:
        """Aplica a técnica SQ3R e retorna um resumo estruturado."""
        sections = [paragraph.strip() for paragraph in text.splitlines() if paragraph.strip()]
        return {
            "survey": sections[:1],
            "question": [],
            "read": sections,
            "recite": [],
            "review": [],
        }

    @staticmethod
    def skimming(text: str) -> List[str]:
        """Retorna a primeira palavra de cada parágrafo não vazio."""
        words = []
        for paragraph in text.splitlines():
            stripped = paragraph.strip()
            if stripped:
                words.append(stripped.split()[0])
        return words

    @staticmethod
    def scanning(text: str, keyword: str) -> List[str]:
        """Busca ocorrências de uma palavra-chave e retorna sentenças correspondentes."""
        sentences = text.split(".")
        return [sentence.strip() for sentence in sentences if keyword.lower() in sentence.lower()]


class RankingUpdater:
    """Atualiza a lista de líderes acadêmicos a partir de um arquivo JSON local."""

    def __init__(self, json_path: str = "rankings.json") -> None:
        self.json_path = json_path

    def update(self) -> Dict[str, str]:
        """Carrega e retorna os rankings locais; se faltar o arquivo, retorna vazio."""
        try:
            with open(self.json_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return {}
        return data if isinstance(data, dict) else {}


@dataclass
class InfinityAtomAgent:
    """Agente integrado que combina emoção, filosofia, ética, memória e leitura."""

    emotion_engine: EmotionEngine = field(default_factory=EmotionEngine)
    philosophy_engine: PhilosophyEngine = field(default_factory=PhilosophyEngine)
    ethics_engine: EthicsEngine = field(default_factory=EthicsEngine)
    scenario_engine: ScenarioEngine = field(default_factory=ScenarioEngine)
    memory_engine: MemoryEngine = field(default_factory=MemoryEngine)
    reading_module: ReadingModule = field(default_factory=ReadingModule)
    ranking_updater: RankingUpdater = field(default_factory=RankingUpdater)

    def analyze_situation(self, situation: Dict[str, Any]) -> Dict[str, Any]:
        """Processa uma situação e retorna um resumo do estado interno do agente."""
        scenarios = self.scenario_engine.generate_scenarios(situation)
        chosen = self.scenario_engine.evaluate_scenarios(scenarios)

        if "evento" in situation:
            self.emotion_engine.adjust("antecipação", 0.1)

        philosophy_scores = self.philosophy_engine.evaluate(situation)

        proposition = situation.get("proposição", "")
        moral_verdict = self.ethics_engine.judge(proposition) if proposition else "n/a"

        self.memory_engine.store(str(situation))

        return {
            "selected_scenario": chosen,
            "dominant_emotion": self.emotion_engine.dominant(),
            "philosophy_scores": philosophy_scores,
            "moral_verdict": moral_verdict,
            "memory_count": len(self.memory_engine.memories),
        }

    def update_rankings(self) -> Dict[str, str]:
        """Atualiza e retorna a lista de líderes acadêmicos conhecida pelo agente."""
        return self.ranking_updater.update()

    def read_text(self, text: str) -> Dict[str, Any]:
        """Processa um texto usando as técnicas de leitura configuradas."""
        return self.reading_module.sq3r(text)

    def recall_memory(self) -> Optional[str]:
        """Recupera uma memória usando o mecanismo de repetição espaçada."""
        return self.memory_engine.recall()

    def simulate_learning(self, subject: str) -> None:
        """Registra um aprendizado e ajusta emoções conforme a experiência."""
        self.memory_engine.store(f"Aprendizado sobre {subject}")
        self.emotion_engine.adjust("alegria", 0.1)
