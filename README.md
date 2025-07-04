# 👋 Gerenciador de Clientes - Guia Rápido

Este projeto é uma aplicação simples feita em **Python** com interface gráfica usando **Tkinter**, e armazenamento de dados via **SQLite**.

---

## 🛠️ Tecnologias Utilizadas
- Python 🐍  
- SQLite 🗃️  
- Tkinter 🖼️  
- PyInstaller (opcional) 💾

---

## 📋 Funcionalidades
- ➕ Adicionar novos clientes  
- 👁️ Visualizar todos os clientes  
- 🔍 Buscar por nome, sobrenome, email ou CPF  
- ✏️ Atualizar dados de clientes  
- 🗑️ Deletar clientes  

---

## 🗂️ Estrutura dos Arquivos

- **`Gui.py`**: Interface gráfica (Tkinter)
- **`Backend.py`**: Conexão e operações com o banco de dados (SQLite)
- **`application.py`**: Arquivo principal que inicializa a aplicação

---

## 🧱 Banco de Dados

O banco de dados é salvo como `clientes.db` com a tabela `clientes`, contendo os seguintes campos:

| Campo      | Tipo     | Descrição                    |
|------------|----------|------------------------------|
| `id`       | INTEGER  | Chave primária (auto) 🔑     |
| `nome`     | TEXT     | Nome do cliente              |
| `sobrenome`| TEXT     | Sobrenome do cliente         |
| `email`    | TEXT     | Email do cliente 📧          |
| `cpf`      | TEXT     | CPF do cliente 🆔            |

---

Criado e Codificado Por: Nicolas Ubaldo Moreira.

Ultima Alteração: 04/07/2025 as 16:20
