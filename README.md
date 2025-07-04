🖱️ Como Usar A Aplicação.
🏷️ Campos de entrada: Nome, Sobrenome, Email, CPF

🔘 Botões:

➕ Adicionar: Insere um novo cliente

✏️ Atualizar: Atualiza o cliente selecionado

🗑️ Deletar: Remove o cliente selecionado

🔍 Buscar: Filtra clientes pelos dados informados

🧹 Limpar: Limpa os campos de entrada

📊 Tabela: Exibe todos os clientes

📋 Passo a passo
➕ Adicionar cliente: Preencha os campos e clique em "Adicionar".

👁️ Visualizar clientes: Tabela mostra todos os clientes automaticamente.

🔍 Buscar clientes: Digite qualquer critério e clique em "Buscar".

✏️ Atualizar cliente: Selecione na tabela, edite os campos e clique em "Atualizar".

🗑️ Deletar cliente: Selecione na tabela e clique em "Deletar".

🛠️ Criando um Executável com PyInstaller
Passos:
📥 Instale o PyInstaller:

pip install pyinstaller
📦 Crie o executável:

cd caminho/para/gerenciador_clientes
pyinstaller --onefile --noconsole application.py
--onefile: gera um único arquivo executável

--noconsole: não abre janela de terminal ao executar

🏃 Execute o arquivo na pasta dist:

Windows: clique duas vezes em application.exe

💡 Dica: O executável pode ser grande (~50-100 MB) pois inclui o Python e dependências. Copie junto o arquivo clientes.db se necessário.

🗄️ Estrutura do Banco de Dados
Banco SQLite salvo em clientes.db com a tabela clientes:

Campo	Tipo	Descrição
id	INTEGER	Identificador único (auto)
nome	TEXT	Nome do cliente
sobrenome	TEXT	Sobrenome do cliente
email	TEXT	Email do cliente
cpf	TEXT	CPF do cliente

O método Backend.initDB() cria a tabela automaticamente na primeira execução.

🛑 Dicas para Solução de Problemas
⚠️ Erro: "No module named tkinter"
Certifique-se que Tkinter está instalado. No Linux, pode instalar com:

pip install tk
🐞 Erro ao executar

Verifique se os arquivos estão na mesma pasta.

Execute python application.py na pasta correta.

🚫 Executável não abre

Confirme que o PyInstaller criou o executável sem erros.

No Windows, execute pelo terminal para ver mensagens:

./dist/application.exe
🔄 Tabela não atualiza

Verifique se o arquivo clientes.db está no local correto.

🎓 Para Alunos: O que você pode aprender com este projeto?
🐍 Python: criação de classes, métodos estáticos, organização em módulos

🗃️ SQL/SQLite: criação e manipulação segura de tabelas e dados

🎨 Tkinter: criação de interfaces gráficas com widgets básicos

✔️ Boas práticas: consultas parametrizadas, separação de camadas, documentação clara

📦 PyInstaller: empacotamento de programas Python em executáveis

🌟 Próximos Passos
Sugestões para evoluir o projeto:

✅ Validação de CPF para formato correto

📤 Exportar lista de clientes para arquivo CSV

🔄 Botão para recarregar clientes após busca

🎨 Melhorar a interface com cores e ícones

Se precisar de ajuda, consulte seu instrutor!

Desenvolvido por: Nicolas Ubaldo Moreira.

ultima vez alterado 04/07/2025 as 15:17






