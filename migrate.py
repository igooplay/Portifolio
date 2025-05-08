import os
import sys
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_migration_command(command=None):
    """
    Executa comandos de migração
    """
    # Verifica se FLASK_APP está configurado
    if not os.environ.get('FLASK_APP'):
        os.environ['FLASK_APP'] = 'app.py'
    
    if command is None or command == 'help':
        print("\n=== Comandos de Migração Disponíveis ===")
        print("python migrate.py init     # Inicializa o repositório de migrações")
        print("python migrate.py migrate  # Cria uma nova migração (também aceita mensagem: 'migrate \"mensagem\"')")
        print("python migrate.py upgrade  # Aplica todas as migrações pendentes")
        print("python migrate.py downgrade # Reverte a migração mais recente")
        print("python migrate.py history  # Mostra o histórico de migrações")
        print("python migrate.py current  # Mostra a revisão atual do banco de dados")
        return
    
    # Extrair o comando principal
    command_parts = command.split(' ', 1)
    main_command = command_parts[0].lower()
    
    # Mapa de comandos para comandos flask-migrate
    command_map = {
        'init': 'flask db init',
        'migrate': 'flask db migrate',
        'upgrade': 'flask db upgrade',
        'downgrade': 'flask db downgrade',
        'history': 'flask db history',
        'current': 'flask db current'
    }
    
    if main_command not in command_map:
        logger.error(f"Comando desconhecido: {main_command}")
        run_migration_command('help')
        return
    
    flask_command = command_map[main_command]
    
    # Adicionar mensagem para comando migrate se fornecida
    if main_command == 'migrate' and len(command_parts) > 1:
        flask_command += f' -m "{command_parts[1]}"'
    
    logger.info(f"Executando: {flask_command}")
    os.system(flask_command)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_migration_command(' '.join(sys.argv[1:]))
    else:
        run_migration_command('help')