import sqlite3


class Home:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()

    def criaer_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Estoque (
                   id ITEGER PRIMARY KEY,
                   Produto TEXT,
                   Quantidade INTEGER
                   )
                ''')
        self.conn.commit()

    def adicionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "ISERT INTO Estoque (Produto, Quantidade) VALUES (?, ?)", (produto, quantidade))
        self.conn.commit()

    def remover_produto(self, produto, quantidade):
        cursor = self.conn.cursor(
        "SELECT quantidade FROM estoque WHERE produto=?", (produto))
        resultado = cursor.fetchone()
        if resultado:
            estoque_atual = resultado[0]
            if estoque_atual >= quantidade:
                cursor.execute("UPDATE estoque SET quantidade=? WHERE produto=?",
                               (estoque_atual - quantidade, produto))
                self.conn.commit()
            else:
                print(f"Quantidade insuficiente de {produto} em estoque.")
        else:
            print(f"{produto} não encontrado em estoque.")

    def 
