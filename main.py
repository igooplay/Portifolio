import os
import logging
from app import app
from seed_data import seed_database

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar os dados se o banco estiver vazio
with app.app_context():
    try:
        # Chamando a função de seed que verifica automaticamente se já existem dados
        seed_database()
        logger.info("Verificação de dados iniciais concluída com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao inicializar dados: {str(e)}")
        # Não interrompa o aplicativo aqui, apenas registre o erro

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
