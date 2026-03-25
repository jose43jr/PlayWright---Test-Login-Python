\# QA Bug Hunt – Login com Playwright (Python)

Projeto focado na identificação de bugs em fluxos críticos de autenticação.

\## Objetivo

Validar comportamentos incorretos no login e demonstrar a importância de testes negativos.

\## Cenários testados

\- Login sem preencher campos

\- Validação de mensagens de erro

\- Comportamento da interface

\## Possíveis impactos (se não testado)

\- Usuários não conseguem acessar o sistema

\- Falta de feedback causa confusão

\- Aumento de chamados no suporte

\- Perda de credibilidade do produto

\## Tecnologias

\- Python

\- Playwright

\## Como executar

```bash

pip install -r requirements.txt

playwright install

python tests/test\_login\_bug.py

```
