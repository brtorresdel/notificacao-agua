# Lembrete para beber água / comer

Fiz esse código em python no trabalho pra me lembrar de beber água e comer nas horas certas. As notificações funcionam assim (é gosto pessoal, mas você pode editar o código pra personalizar os horários, se preferir):

- **Lembrete de Água:** Envia uma notificação a cada **30 minutos**. O ciclo de notificação é programado para começar nos minutos **:20** e **:50** de cada hora (ex: 09:20, 09:50, 10:20, etc.).
- **Lembrete de Comida/Lanche:** Envia uma notificação a cada **3 horas**, ideal para lembrá-lo de fazer pequenos lanches ou refeições intermediárias. A rotina é programada para começar às **09:00** (ex: 09:00, 12:00, 15:00, 18:00).

O script utiliza a programação assíncrona (`asyncio`) para gerenciar as duas rotinas de lembretes de forma concorrente.

## 🚀 Instalação e Execução

### 1. Pré-requisitos

Para executar este script, você precisa ter o **Python** instalado na sua máquina (versão 3.6+ é recomendada).

### 2. Dependências

O script utiliza a biblioteca `notifypy` para enviar notificações nativas do sistema operacional.

Instale a biblioteca necessária via `pip`:

```bash
pip install notifypy
