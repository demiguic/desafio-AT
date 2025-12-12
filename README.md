# Desafio Técnico — Processo Seletivo

Aplicação desenvolvida em Django como parte de um processo seletivo.
O objetivo é permitir que investidores registrem e acompanhem seus ativos financeiros, além de configurar gatilhos de compra/venda com notificação por e-mail e atualização automática de preços.

---

## 🎯 Funcionalidades

### Gestão de Ativos
- Cadastro de ativos (stocks, criptos ou outros).
- Registro de preço de compra, quantidade e tipo de operação.
- Interface simples para visualizar performance básica.

### Gatilhos de Monitoramento
O usuário pode configurar:
- Preço alvo da venda;
- Preço alvo da compra.
  
Quando o preço do mercado atinge o valor configurado, o sistema dispara uma notificação via SMTP.

### Atualização Automática (Cronjob / Redis)

- O usuário define a frequência de atualização para cada ativo individualmente.
- Uma tarefa assíncrona (via Redis, Celery ) atualiza os preços periodicamente.
- Integração com API de mercado financeiro (yfinance).

### Notificação por E-mail

- Envio automático quando um target é atingido.
- Configurável pelo arquivo .env.
---

## 🛠️ Tecnologias Utilizadas
- Django (backend principal)
- Django ORM
- Redis
- Celery
- Requests (para chamada à API de preços)
- SMTP (notificação)

---

## Arquitetura
```
/desafio-AT
 ├── core/               # Configurações principais
 ├── assets/             # App responsável pelos ativos
 ├── triggers/           # Regras de gatilho (preço-alvo)
 ├── scheduler/          # Integração com Redis / tarefas
 ├── templates/          # HTML das telas
 ├── static/             # CSS/JS
 ├── requirements.txt
 └── manage.py

```

## Licença
Projeto desenvolvido exclusivamente para fins de avaliação técnica.
