import sqlite3 as sql  # Importa a biblioteca sqlite3 para gerenciar o banco de dados SQLite

# Define a classe Backend para gerenciar as operações com o banco de dados
class Backend:
    # Variáveis de classe (compartilhadas por todas as instâncias da classe)
    database = "clientes.db"  # Nome do arquivo do banco de dados
    conn = None  # Conexão com o banco de dados (inicialmente vazia)
    cur = None   # Cursor para executar comandos SQL (inicialmente vazio)
    connected = False  # Indica se a conexão com o banco está ativa

    # Método para conectar ao banco de dados
    def connect(self):
        # Cria uma conexão com o banco de dados especificado em 'database'
        Backend.conn = sql.connect(Backend.database)
        # Cria um cursor para executar comandos SQL
        Backend.cur = Backend.conn.cursor()
        # Marca a conexão como ativa
        Backend.connected = True

    # Método para desconectar do banco de dados
    def disconnect(self):
        # Fecha a conexão com o banco de dados
        Backend.conn.close()
        # Marca a conexão como inativa
        Backend.connected = False

    # Método para executar comandos SQL
    def execute(self, sql, parms=None):
        # Verifica se a conexão está ativa
        if Backend.connected:
            # Se não houver parâmetros, executa o comando SQL diretamente
            if parms is None:
                Backend.cur.execute(sql)
            # Caso contrário, executa o comando SQL com os parâmetros fornecidos
            else:
                Backend.cur.execute(sql, parms)
            return True  # Retorna True se a execução for bem-sucedida
        else:
            return False  # Retorna False se não houver conexão ativa

    # Método para recuperar todos os resultados de uma consulta
    def fetchall(self):
        # Retorna todas as linhas retornadas pela última consulta SQL
        return Backend.cur.fetchall()

    # Método para salvar (commit) as alterações no banco de dados
    def persist(self):
        # Verifica se a conexão está ativa
        if Backend.connected:
            # Salva as alterações no banco de dados
            Backend.conn.commit()
            return True  # Retorna True se o commit for bem-sucedido
        else:
            return False  # Retorna False se não houver conexão ativa

    # Método estático para inicializar o banco de dados
    @staticmethod
    def initDB():
        # Cria uma nova instância da classe Backend
        backend = Backend()
        # Conecta ao banco de dados
        backend.connect()
        # Cria uma tabela 'clientes' se ela ainda não existir
        # A tabela tem colunas: id (chave primária), nome, sobrenome, email e cpf
        backend.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        # Salva as alterações
        backend.persist()
        # Desconecta do banco de dados
        backend.disconnect()

    # Método estático para inserir um novo cliente no banco de dados
    @staticmethod
    def insert(nome, sobrenome, email, cpf):
        # Cria uma nova instância da classe
        backend = Backend()
        # Conecta ao banco de dados
        backend.connect()
        # Insere um novo registro na tabela clientes
        # NULL é usado para o id, pois ele é gerado automaticamente (PRIMARY KEY)
        backend.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        # Salva as alterações
        backend.persist()
        # Desconecta do banco de dados
        backend.disconnect()

    # Método estático para visualizar todos os clientes
    @staticmethod
    def view():
        # Cria uma nova instância da classe
        backend = Backend()
        # Conecta ao banco de dados
        backend.connect()
        # Executa uma consulta para selecionar todos os registros da tabela clientes
        backend.execute("SELECT * FROM clientes")
        # Recupera todas as linhas retornadas
        rows = backend.fetchall()
        # Desconecta do banco de dados
        backend.disconnect()
        # Retorna a lista de clientes
        return rows

    # Método estático para buscar clientes com base em critérios
    @staticmethod
    def search(nome="", sobrenome="", email="", cpf=""):
        # Cria uma nova instância da classe
        backend = Backend()
        # Conecta ao banco de dados
        backend.connect()
        # Executa uma consulta para buscar clientes que correspondam aos critérios
        # Usa OR para buscar em qualquer uma das colunas (nome, sobrenome, email ou cpf)
        backend.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
        # Recupera todas as linhas retornadas
        rows = backend.fetchall()
        # Desconecta do banco de dados
        backend.disconnect()
        # Retorna a lista de clientes encontrados
        return rows

    # Método estático para deletar um cliente pelo ID
    @staticmethod
    def delete(id):
        # Cria uma nova instância da classe
        backend = Backend()
        # Conecta ao banco de dados
        backend.connect()
        # Executa um comando para deletar o cliente com o ID especificado
        backend.execute("DELETE FROM clientes WHERE id = ?", (id,))
        # Salva as alterações
        backend.persist()
        # Desconecta do banco de dados
        backend.disconnect()

    # Método estático para atualizar os dados de um cliente pelo ID
    @staticmethod
    def update(id, nome, sobrenome, email, cpf):
        # Cria uma nova instância da classe
        backend = Backend()
        # Conecta ao banco de dados
        backend.connect()
        # Executa um comando para atualizar os dados do cliente com o ID especificado
        backend.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
        # Salva as alterações
        backend.persist()
        # Desconecta do banco de dados
        backend.disconnect()