import os
import logging
from flask_migrate import Migrate
from app import app, db

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Migrate já está configurado em app.py
# Esta é apenas uma interface de linha de comando para gerenciar migrações

def print_migration_help():
    """Exibe ajuda sobre os comandos de migração"""
    logger.info("\n=== Gerenciador de Migrações do SeuCodigo ===")
    logger.info("Use os seguintes comandos para gerenciar migrações do banco de dados:")
    logger.info("")
    logger.info("flask db init")
    logger.info("  Inicializa a estrutura de migrações (execute apenas uma vez)")
    logger.info("")
    logger.info("flask db migrate -m \"descrição da migração\"")
    logger.info("  Cria uma nova migração baseada nas mudanças nos modelos")
    logger.info("")
    logger.info("flask db upgrade")
    logger.info("  Aplica as migrações pendentes no banco de dados")
    logger.info("")
    logger.info("flask db downgrade")
    logger.info("  Reverte a migração mais recente")
    logger.info("")
    logger.info("flask db history")
    logger.info("  Mostra o histórico de migrações")
    logger.info("\n=== Como usar ===")
    logger.info("1. Modifique seus modelos em models.py")
    logger.info("2. Execute 'flask db migrate -m \"descrição da mudança\"'")
    logger.info("3. Verifique o arquivo de migração gerado na pasta 'migrations'")
    logger.info("4. Execute 'flask db upgrade' para aplicar as mudanças")

if __name__ == "__main__":
    print_migration_help()
    
    # Tentativa de executar o comando flask db diretamente
    try:
        os.system("flask db")
    except Exception as e:
        logger.error(f"Erro ao executar comando flask db: {str(e)}")
        logger.info("Execução manual dos comandos é necessária.")