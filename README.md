# Game

Prompt builder em Python para um agente de arte de elite capaz de transformar um tema em um prompt visual técnico, denso e cinematográfico.

## Uso

```python
from master_art_architect import SYSTEM_PROMPT, build_image_prompt

print(SYSTEM_PROMPT)
print(build_image_prompt("uma cidade cyberpunk à noite"))
```

## Testes

```bash
python -m unittest discover -s tests
```
