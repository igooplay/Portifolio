# Migração de Banco de Dados PostgreSQL → MySQL

Este guia explica como migrar seu projeto do banco de dados PostgreSQL para MySQL.

## Pré-requisitos

1. Servidor MySQL instalado e funcionando
2. Acesso administrativo ao servidor MySQL
3. Python e as dependências necessárias instaladas

## Passos para migração

### 1. Configurar as variáveis de ambiente do MySQL

Defina as seguintes variáveis de ambiente com as informações do seu servidor MySQL:

```bash
export MYSQL_USER=seu_usuario
export MYSQL_PASSWORD=sua_senha
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_DATABASE=seucodigo
```

### 2. Criar o banco de dados MySQL

Execute o script para criar o banco de dados MySQL:

```bash
python create_mysql_db.py
```

Este script verifica se o banco de dados já existe e o cria se necessário, usando as configurações definidas em `mysql_config.py`.

### 3. Exportar dados do PostgreSQL

Primeiro, certifique-se de que o PostgreSQL está configurado através da variável de ambiente `DATABASE_URL`. Em seguida, exporte todos os dados:

```bash
python db_migration.py export
```

Este comando exportará todos os dados do banco PostgreSQL para arquivos JSON que podem ser usados para importação posterior.

### 4. Alterar a configuração para MySQL

Para usar o MySQL, basta não definir a variável de ambiente `DATABASE_URL`. O sistema automaticamente usará a configuração MySQL definida em `mysql_config.py`.

```bash
unset DATABASE_URL  # ou remova a variável de ambiente
```

### 5. Importar dados para MySQL

Agora, importe os dados dos arquivos JSON para o MySQL:

```bash
python db_migration.py import
```

### 6. Verificar a migração

Inicie o aplicativo e verifique se tudo está funcionando corretamente. O aplicativo deve estar usando o banco de dados MySQL, e todos os dados devem ter sido migrados corretamente.

## Alternando entre PostgreSQL e MySQL

- Para usar PostgreSQL: defina a variável de ambiente `DATABASE_URL` com a URL de conexão PostgreSQL
- Para usar MySQL: não defina a variável `DATABASE_URL`, o sistema usará a configuração em `mysql_config.py`

## Personalizando a configuração MySQL

Se precisar personalizar as configurações do MySQL, edite o arquivo `mysql_config.py`. Você pode alterar:

- Usuário, senha, host e porta
- Nome do banco de dados
- Charset e collation (UTF-8 por padrão)
- Outras configurações de conexão

## Solução de problemas

### Erro de conexão com MySQL

Verifique se:
- O servidor MySQL está em execução
- As credenciais estão corretas
- O banco de dados existe
- O usuário tem permissões para acessar o banco de dados

### Erro durante a importação de dados

- Certifique-se de que exportou os dados corretamente do PostgreSQL
- Verifique se os arquivos JSON exportados existem
- Verifique se há erros no formato dos dados

### Diferenças de sintaxe entre PostgreSQL e MySQL

PostgreSQL e MySQL têm algumas diferenças na sintaxe SQL. Se você estiver usando consultas SQL personalizadas no código, pode precisar ajustá-las para funcionar com ambos os sistemas. SQLAlchemy geralmente lida com essas diferenças automaticamente, mas consultas SQL não parametrizadas podem precisar de ajustes.