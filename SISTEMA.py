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

    def consultar_estoque(self, produto):
        cursor = self.conn.fetchone()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return 0
        
    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT produto FROM estoque")
        produtos = cursor.fetchall()
        return [produto[0] for produto in produtos]
    
sistema = Home("Estoque.db")

sistema.adicionar_produto("Mangá: Jujutsu Kaisen volume 1", 50)
sistema.adicionar_produto("Mangá: YuYu Hakusho volume 1", 49)
sistema.adicionar_produto("Mangá: JoJo's Bizarre Adventures - Parte 6: Stone Ocean volume 1", 25)

estoque_manga = sistema.consultar_estoque("Mangás")
print(f"Quantidade de Mangás em estoque: {estoque_manga}")


sistema.remover_produto("Mangá: JoJo's Bizarre Adventures - Parte 6: Stone Ocean volume 1", 10)
print("Estoque de Mangás alterados com sucesso!")

produtos_em_estoque = sistema.listar_produtos()
print(f"Produtos em estoque: {produtos_em_estoque}")
