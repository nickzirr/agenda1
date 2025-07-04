import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from Gui import Gui  # Importa a classe Gui para a interface
from Backend import Backend  # Importa a classe Backend para inicializar o banco de dados

# Função principal para iniciar a aplicação
def main():
    # Inicializa o banco de dados chamando o método estático initDB
    Backend.initDB()
    
    # Cria a janela principal do Tkinter
    root = tk.Tk()
    # Cria uma instância da classe Gui, passando a janela principal
    app = Gui(root)
    # Inicia o loop principal da aplicação (mantém a janela aberta)
    root.mainloop()

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()