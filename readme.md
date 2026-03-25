# QA Bug Hunt – Login com Playwright (Python)

Projeto focado na identificação de comportamentos incorretos em fluxos críticos de autenticação.

## Objetivo

Validar cenários negativos no login, garantindo que o sistema trate corretamente entradas inválidas e forneça feedback adequado ao usuário.

## Cenários testados

- Login sem preenchimento de usuário e senha
- Validação da exibição de mensagens de erro
- Comportamento da interface diante de entradas inválidas

## Possíveis impactos (se não testado)

- Usuários impedidos de acessar o sistema
- Falta de feedback, gerando confusão
- Aumento de chamados no suporte
- Impacto na experiência do usuário e credibilidade do produto

## Tecnologias

- Python
- Playwright
- Pytest

## Como executar

```bash
pip install -r requirements.txt
python -m playwright install
python -m pytest tests/test_login_bug.py --headed --slowmo=500
```
