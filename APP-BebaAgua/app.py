import time
from plyer import notification

def lembrar_beber_agua(intervalo):
    while True:
        # Exibe uma notificação para o usuário beber água
        notification.notify(
            title="Lembrete: Beba água!",
            message="Lembre-se de beber água regularmente.",
            app_icon=None,  # Caminho para um ícone personalizado (opcional)
            timeout=10  # Tempo em segundos para a notificação desaparecer automaticamente
        )
        
        # Pausa o programa pelo intervalo de tempo definido em segundos
        time.sleep(intervalo)

# Define o intervalo de tempo para lembrar o usuário (em segundos)
intervalo = 3600  # Lembrete a cada 1 hora

lembrar_beber_agua(intervalo)