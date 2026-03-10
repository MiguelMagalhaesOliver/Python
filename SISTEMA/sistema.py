import sqlite3


class Home:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()

    def criar_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Produto TEXT UNIQUE,
                Quantidade INTEGER
            )
        """)
        self.conn.commit()

    def adicionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT Quantidade FROM Estoque WHERE Produto=?",
            (produto,)
        )
        resultado = cursor.fetchone()

        if resultado:
            nova_qtd = resultado[0] + quantidade
            cursor.execute(
                "UPDATE Estoque SET Quantidade=? WHERE Produto=?",
                (nova_qtd, produto)
            )
        else:
            cursor.execute(
                "INSERT INTO Estoque (Produto, Quantidade) VALUES (?, ?)",
                (produto, quantidade)
            )

        self.conn.commit()

    def remover_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT Quantidade FROM Estoque WHERE Produto=?",
            (produto,)
        )

        resultado = cursor.fetchone()

        if resultado:
            estoque_atual = resultado[0]

            if estoque_atual >= quantidade:
                cursor.execute(
                    "UPDATE Estoque SET Quantidade=? WHERE Produto=?",
                    (estoque_atual - quantidade, produto)
                )
                self.conn.commit()
            else:
                print("Quantidade insuficiente.")
        else:
            print("Produto não encontrado.")

    def consultar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT Quantidade FROM Estoque WHERE Produto=?",
            (produto,)
        )

        resultado = cursor.fetchone()
        return resultado[0] if resultado else 0

    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT Produto FROM Estoque")
        return [p[0] for p in cursor.fetchall()]