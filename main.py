import asyncio
import datetime
import time
from notifypy import Notify

# --- Funções de Notificação ---
def enviar_notificacao(titulo, mensagem):
    """Função genérica para enviar notificações."""
    n = Notify()
    n.title = titulo
    n.message = mensagem
    n.send()
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Notificação enviada: {titulo}")

# --- Tarefas Assíncronas ---

async def lembrete_agua():
    """Gerencia as notificações de água a cada 30 minutos, começando nos minutos 20 ou 50."""
    print("Aguardando o horário de início para lembrete de água (minutos 20 ou 50)...")
    while True:
        agora = datetime.datetime.now()
        if agora.minute == 20 or agora.minute == 50:
            print(f"[{agora.strftime('%H:%M:%S')}] Horário de início para água alcançado.")
            break
        await asyncio.sleep(1) # Espera assíncrona

    # Primeira notificação de água
    enviar_notificacao("Vamos se hidratar?", "Tá na hora de beber água, bora!")

    # Loop principal para notificações de água a cada 30 minutos
    while True:
        # Verifica se o minuto atual é 20 ou 50 para evitar atrasos no primeiro ciclo
        agora = datetime.datetime.now()
        minuto_atual = agora.minute
        
        # Calcula o tempo restante até o próximo minuto 20 ou 50
        proximo_minuto = 20 if minuto_atual < 20 or (minuto_atual > 50 and minuto_atual < 80) else 50
        
        # Garante que o cálculo é para o futuro
        if proximo_minuto <= minuto_atual:
             if proximo_minuto == 20: # Se estamos no minuto 50 e o próximo é 20, pulamos para a próxima hora
                 tempo_espera_segundos = (60 - minuto_atual + 20) * 60 - agora.second
             else: # Se estamos no minuto 20 e o próximo é 50
                 tempo_espera_segundos = (50 - minuto_atual) * 60 - agora.second
        else: # Se o próximo minuto é maior que o atual na mesma hora
            tempo_espera_segundos = (proximo_minuto - minuto_atual) * 60 - agora.second
        
        # Garante um mínimo de espera para não notificar imediatamente se já for o minuto
        if tempo_espera_segundos <= 0:
            tempo_espera_segundos = 30 * 60 # Espera 30 minutos se já passou do tempo

        print(f"[{agora.strftime('%H:%M:%S')}] Próxima notificação de água em ~{round(tempo_espera_segundos / 60)} minutos.")
        await asyncio.sleep(tempo_espera_segundos)
        enviar_notificacao("Vamos se hidratar?", "Tá na hora de beber água, bora!")

async def lembrete_comida():
    """Gerencia as notificações de comida a cada 3 horas, começando às 09:00."""
    print("Aguardando o horário de início para lembrete de comida (09:00)...")
    while True:
        agora = datetime.datetime.now()
        if agora.hour == 9 or agora.hour == 12 or agora.hour == 15 or agora.hour == 18: # Começa a partir das 09:00 no minuto 0
            print(f"[{agora.strftime('%H:%M:%S')}] Horário de início para comida alcançado.")
            break
        await asyncio.sleep(1) # Espera assíncrona

    # Primeira notificação de comida
    enviar_notificacao("Hora de Comer!", "Faça um lanche saudável ou uma refeição!")

    # Loop principal para notificações de comida a cada 3 horas
    while True:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Próxima notificação de comida em 3 horas.")
        await asyncio.sleep(3 * 3600) # 3 horas em segundos
        enviar_notificacao("Hora de Comer!", "Faça um lanche saudável ou uma refeição!")

# --- Execução Principal Assíncrona ---
async def main():
    # Roda as duas tarefas concorrentemente
    await asyncio.gather(
        lembrete_agua(),
        lembrete_comida()
    )

if __name__ == "__main__":
    asyncio.run(main())
