import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import ttk, messagebox  # Importa componentes adicionais do Tkinter
from Backend import Backend  # Importa a classe Backend para interagir com o banco de dados

# Define a classe Gui para gerenciar a interface gráfica
class Gui:
    def __init__(self, root):
        # 'root' é a janela principal da aplicação
        self.root = root
        self.root.title("Gerenciador de Clientes")  # Define o título da janela
        self.backend = Backend()  # Cria uma instância da classe Backend

        # Configura o layout principal da janela
        self.root.geometry("1040x500")  # Define o tamanho da janela (700x500 pixels)
        self.root.resizable(True, False)  # Impede que a janela seja redimensionada

        # Cria os campos de entrada e botões
        self.create_widgets()
        # Cria a área de visualização (Treeview)
        self.create_treeview()
        # Atualiza a Treeview com os dados do banco
        self.update_treeview()

    # Método para criar os campos de entrada e botões
    def create_widgets(self):
        # Frame para os campos de entrada
        input_frame = ttk.LabelFrame(self.root, text="Dados do Cliente")
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Labels e Entries para os campos de entrada
        ttk.Label(input_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = ttk.Entry(input_frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Sobrenome:").grid(row=0, column=2, padx=5, pady=5)
        self.sobrenome_entry = ttk.Entry(input_frame)
        self.sobrenome_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(input_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="CPF:").grid(row=1, column=2, padx=5, pady=5)
        self.cpf_entry = ttk.Entry(input_frame)
        self.cpf_entry.grid(row=1, column=3, padx=5, pady=5)

        # Frame para os botões
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Botões para as operações
        ttk.Button(button_frame, text="Adicionar", command=self.add_client).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Atualizar", command=self.update_client).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Deletar", command=self.delete_client).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Buscar", command=self.search_client).grid(row=0, column=3, padx=5)
        ttk.Button(button_frame, text="Limpar", command=self.clear_entries).grid(row=0, column=4, padx=5)

    # Método para criar a Treeview (tabela para exibir os clientes)
    def create_treeview(self):
        # Frame para a Treeview
        tree_frame = ttk.LabelFrame(self.root, text="Lista de Clientes")
        tree_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Configura a Treeview com colunas
        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Nome", "Sobrenome", "Email", "CPF"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Sobrenome", text="Sobrenome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("CPF", text="CPF")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Adiciona uma barra de rolagem
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Permite selecionar um item da Treeview
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    # Método para atualizar a Treeview com os dados do banco
    def update_treeview(self):
        # Limpa a Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Obtém todos os clientes do banco de dados
        clients = self.backend.view()
        # Adiciona cada cliente à Treeview
        for client in clients:
            self.tree.insert("", "end", values=client)

    # Método chamado ao selecionar um item na Treeview
    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            # Preenche os campos de entrada com os dados do cliente selecionado
            values = self.tree.item(selected_item)["values"]
            self.clear_entries()
            self.nome_entry.insert(0, values[1])
            self.sobrenome_entry.insert(0, values[2])
            self.email_entry.insert(0, values[3])
            self.cpf_entry.insert(0, values[4])

    # Método para adicionar um novo cliente
    def add_client(self):
        # Obtém os valores dos campos de entrada
        nome = self.nome_entry.get()
        sobrenome = self.sobrenome_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()

        # Verifica se todos os campos estão preenchidos
        if nome and sobrenome and email and cpf:
            self.backend.insert(nome, sobrenome, email, cpf)
            self.update_treeview()
            self.clear_entries()
            messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    # Método para atualizar um cliente
    def update_client(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Obtém o ID do cliente selecionado
            id = self.tree.item(selected_item)["values"][0]
            nome = self.nome_entry.get()
            sobrenome = self.sobrenome_entry.get()
            email = self.email_entry.get()
            cpf = self.cpf_entry.get()

            # Verifica se todos os campos estão preenchidos
            if nome and sobrenome and email and cpf:
                self.backend.update(id, nome, sobrenome, email, cpf)
                self.update_treeview()
                self.clear_entries()
                messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            messagebox.showerror("Erro", "Selecione um cliente para atualizar!")

    # Método para deletar um cliente
    def delete_client(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Obtém o ID do cliente selecionado
            id = self.tree.item(selected_item)["values"][0]
            self.backend.delete(id)
            self.update_treeview()
            self.clear_entries()
            messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
        else:
            messagebox.showerror("Erro", "Selecione um cliente para deletar!")

    # Método para buscar clientes
    def search_client(self):
        nome = self.nome_entry.get()
        sobrenome = self.sobrenome_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()
        # Busca no banco de dados com os critérios fornecidos
        clients = self.backend.search(nome, sobrenome, email, cpf)
        # Limpa a Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Adiciona os resultados à Treeview
        for client in clients:
            self.tree.insert("", "end", values=client)

    # Método para limpar os campos de entrada
    def clear_entries(self):
        self.nome_entry.delete(0, tk.END)
        self.sobrenome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)