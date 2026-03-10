import tkinter as tk
from tkinter import messagebox


class Painel:
    def __init__(self, sistema):
        self.sistema = sistema

        self.janela = tk.Tk()
        self.janela.title("Sistema de Estoque")
        self.janela.geometry("400x450")

        # Produto
        tk.Label(self.janela, text="Produto").pack(pady=5)
        self.produto = tk.Entry(self.janela, width=35)
        self.produto.pack()

        # Quantidade
        tk.Label(self.janela, text="Quantidade").pack(pady=5)
        self.quantidade = tk.Entry(self.janela, width=20)
        self.quantidade.pack()

        # Botões
        tk.Button(self.janela, text="Adicionar Produto",
                  command=self.adicionar).pack(pady=5)

        tk.Button(self.janela, text="Remover Produto",
                  command=self.remover).pack(pady=5)

        tk.Button(self.janela, text="Consultar Estoque",
                  command=self.consultar).pack(pady=5)

        tk.Button(self.janela, text="Atualizar Lista",
                  command=self.atualizar_lista).pack(pady=10)

        # Lista
        tk.Label(self.janela, text="Produtos em Estoque").pack()

        self.lista = tk.Listbox(self.janela, width=45, height=10)
        self.lista.pack(pady=5)

        self.atualizar_lista()

        self.janela.mainloop()

    # =========================

    def pegar_dados(self):
        produto = self.produto.get().strip()

        if not produto:
            messagebox.showerror("Erro", "Digite um produto.")
            return None, None

        try:
            quantidade = int(self.quantidade.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser número.")
            return None, None

        return produto, quantidade

    def adicionar(self):
        produto, qtd = self.pegar_dados()
        if produto is None:
            return

        self.sistema.adicionar_produto(produto, qtd)
        messagebox.showinfo("Sucesso", "Produto adicionado!")
        self.atualizar_lista()

    def remover(self):
        produto, qtd = self.pegar_dados()
        if produto is None:
            return

        self.sistema.remover_produto(produto, qtd)
        messagebox.showinfo("Sucesso", "Produto removido!")
        self.atualizar_lista()

    def consultar(self):
        produto = self.produto.get().strip()

        if not produto:
            messagebox.showerror("Erro", "Digite um produto.")
            return

        qtd = self.sistema.consultar_estoque(produto)
        messagebox.showinfo("Estoque", f"Quantidade disponível: {qtd}")

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)

        produtos = self.sistema.listar_produtos()

        for produto in produtos:
            qtd = self.sistema.consultar_estoque(produto)
            self.lista.insert(tk.END, f"{produto} — {qtd} unidades")