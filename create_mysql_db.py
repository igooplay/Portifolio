import os
import pymysql
import mysql_config

def create_database():
    """Cria o banco de dados MySQL se ele não existir."""
    connection = None
    
    try:
        # Conecta ao servidor MySQL sem especificar um banco de dados
        connection = pymysql.connect(
            host=mysql_config.MYSQL_HOST,
            port=int(mysql_config.MYSQL_PORT),
            user=mysql_config.MYSQL_USER,
            password=mysql_config.MYSQL_PASSWORD
        )
        
        with connection.cursor() as cursor:
            # Verifica se o banco de dados já existe
            cursor.execute(f"SHOW DATABASES LIKE '{mysql_config.MYSQL_DATABASE}';")
            result = cursor.fetchone()
            
            # Se o banco de dados não existir, cria-o
            if not result:
                print(f"Criando banco de dados '{mysql_config.MYSQL_DATABASE}'...")
                cursor.execute(f"CREATE DATABASE {mysql_config.MYSQL_DATABASE} CHARACTER SET {mysql_config.MYSQL_CHARSET} COLLATE {mysql_config.MYSQL_COLLATION};")
                print(f"Banco de dados '{mysql_config.MYSQL_DATABASE}' criado com sucesso!")
            else:
                print(f"Banco de dados '{mysql_config.MYSQL_DATABASE}' já existe.")
            
            # Concede todos os privilégios ao usuário no banco de dados
            cursor.execute(f"GRANT ALL PRIVILEGES ON {mysql_config.MYSQL_DATABASE}.* TO '{mysql_config.MYSQL_USER}'@'%';")
            cursor.execute("FLUSH PRIVILEGES;")
            print(f"Privilégios concedidos ao usuário '{mysql_config.MYSQL_USER}'.")
        
        connection.commit()
    
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")
    
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()