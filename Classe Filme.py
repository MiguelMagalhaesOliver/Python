class filme:
    def __init__(self, titulo, genero, ano, diretor, elenco):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.diretor = diretor
        self.elenco = elenco

    def filme_assistir(self):
            print(f"Assistir ao filme {self.titulo}...")

    def adicionar_favoritos(self):
        print(f"O Filme {self.titulo} foi adicionado aos favoritos!")
print(f"--------------------------------------------")
filme1 = filme("Chainsaw Man: O Filme - Arco da Reze", "Terror/Animação", 2025, "Tatsuya Yoshihara", "Reina Ueda")
print(f"Filme: {filme1.titulo}\nGênero: {filme1.genero}\nAno: {filme1.ano}\nDiretor: {filme1.diretor}\nElenco: {filme1.elenco}")
print(f"--------------------------------------------")
filme2 = filme("Jujutsu Kaisen - Execução", "Ação/Terror/Animação", 2025, "Shouta Goshozono", "Junya Enoki")
filme2.Assistir()
filme3 = filme("O Livro de Eli","Ação e Ficção Cientifica",2010,"Albert e Allen Hughes","Denzel Washington")
filme2.adicionar_favorito()
